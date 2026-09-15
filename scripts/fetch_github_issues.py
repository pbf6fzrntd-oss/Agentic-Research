#!/usr/bin/env python3
"""Fetch GitHub issues for a repo within a date window via the plain REST API.

This is the reusable, portable version of the tooling used to build
data/raw/*.json for this project. In the sandboxed research environment
this project was built in, direct calls to api.github.com are blocked by
the session's network policy (confirmed: 403 at the proxy layer, distinct
from GitHub auth) -- that data was instead pulled through the GitHub MCP
tool available in that environment and saved to data/raw/ by hand. This
script exists so the same refresh can be run later from a normal machine
or CI job with real network access, without a new dependency: it uses only
the standard library (urllib) plus a GitHub token.

Usage:
    export GITHUB_TOKEN=ghp_...
    python3 scripts/fetch_github_issues.py --owner anthropics --repo claude-code \\
        --since 2026-07-15 --until 2026-09-15 --out data/raw/github_claude_code.json

    # Optionally narrow with GitHub search qualifiers appended to the query:
    python3 scripts/fetch_github_issues.py --owner freqtrade --repo freqtrade \\
        --since 2026-07-15 --query "label:bug" --out data/raw/github_freqtrade_bugs.json

Notes:
  - Uses the Search API (/search/issues) so it can filter by created-date
    range and sort by interactions/comments/reactions in one call, same as
    the interactive tool this project actually used.
  - Unauthenticated requests are rate-limited to 60/hour; set GITHUB_TOKEN
    (a fine-grained PAT with public-repo read is enough) to raise that to
    5000/hour.
  - Paginates automatically up to --max-pages (default 5 x 100 = 500 items).
"""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.parse
import urllib.error

API_ROOT = "https://api.github.com"


def build_query(owner, repo, since, until, extra_query):
    parts = [f"repo:{owner}/{repo}", "is:issue", f"created:{since}..{until}"]
    if extra_query:
        parts.append(extra_query)
    return " ".join(parts)


def fetch_page(query, page, per_page, sort, order, token):
    params = {
        "q": query,
        "page": str(page),
        "per_page": str(per_page),
    }
    if sort:
        params["sort"] = sort
        params["order"] = order or "desc"
    url = f"{API_ROOT}/search/issues?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--owner", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--since", required=True, help="YYYY-MM-DD, inclusive")
    ap.add_argument("--until", required=True, help="YYYY-MM-DD, inclusive")
    ap.add_argument("--query", default="", help="Extra GitHub search qualifiers, e.g. 'label:bug'")
    ap.add_argument("--sort", default="created", choices=["created", "updated", "comments", "reactions", "interactions"])
    ap.add_argument("--order", default="desc", choices=["asc", "desc"])
    ap.add_argument("--per-page", type=int, default=100)
    ap.add_argument("--max-pages", type=int, default=5)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print("WARNING: no GITHUB_TOKEN/GH_TOKEN set — limited to 60 requests/hour unauthenticated",
              file=sys.stderr)

    query = build_query(args.owner, args.repo, args.since, args.until, args.query)
    print(f"query: {query}", file=sys.stderr)

    all_items = []
    for page in range(1, args.max_pages + 1):
        try:
            data = fetch_page(query, page, args.per_page, args.sort, args.order, token)
        except urllib.error.HTTPError as e:
            print(f"HTTP {e.code} on page {page}: {e.read().decode('utf-8', 'replace')}", file=sys.stderr)
            break
        items = data.get("items", [])
        all_items.extend(items)
        print(f"page {page}: {len(items)} items (total_count={data.get('total_count')})", file=sys.stderr)
        if len(items) < args.per_page:
            break
        time.sleep(1)  # be polite to the search API's stricter rate limit

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"query": query, "fetched_count": len(all_items), "items": all_items}, f, indent=2)
    print(f"wrote {len(all_items)} items to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
