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
from datetime import date, datetime, timezone
from atomic import atomic_text
import argparse
import json
import os
import sys
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
        raw = resp.read(8_000_001)
        if len(raw) > 8_000_000:
            raise ValueError("Oversized search page")
        return json.loads(raw.decode("utf-8"))


def collect(query, per_page=100, max_pages=5, sort="created", order="desc", token=None, fetcher=fetch_page):
    items_by_id = {}
    total = None
    problems = []
    fetched_pages = []
    for page in range(1, max_pages + 1):
        try:
            data = fetcher(query, page, per_page, sort, order, token)
            if not isinstance(data.get("items"), list) or type(data.get("total_count")) is not int or data["total_count"] < 0:
                raise ValueError("Invalid search response")
            if total is not None and total != data["total_count"]:
                problems.append("total_count changed during pagination")
            total = data["total_count"]
            if data.get("incomplete_results") is not False:
                problems.append(f"page {page}: incomplete_results or missing completeness flag")
            for item in data["items"]:
                key = item.get("id")
                if type(key) is not int or not item.get("html_url"):
                    raise ValueError("Invalid issue identity")
                if key in items_by_id:
                    problems.append(f"duplicate issue identity on page {page}")
                items_by_id[key] = item
            fetched_pages.append(page)
            if len(data["items"]) < per_page or len(items_by_id) >= total:
                break
        except (urllib.error.URLError, ValueError, KeyError, TypeError) as error:
            problems.append(f"page {page} failed: {type(error).__name__}")
            break
    if total is None or len(items_by_id) != total:
        problems.append("unique fetched count does not match total_count")
    if total is not None and total > 1000:
        problems.append("GitHub search ceiling exceeded; split the observation window")
    return {"query":query,"fetched_at":datetime.now(timezone.utc).isoformat(),"total_count":total,"fetched_count":len(items_by_id),"pages":fetched_pages,"complete":not problems,"problems":problems,"items":list(items_by_id.values())}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--owner", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--since", required=True)
    ap.add_argument("--until", required=True)
    ap.add_argument("--query", default="")
    ap.add_argument("--sort", default="created", choices=["created", "updated", "comments", "reactions", "interactions"])
    ap.add_argument("--order", default="desc", choices=["asc", "desc"])
    ap.add_argument("--per-page", type=int, default=100)
    ap.add_argument("--max-pages", type=int, default=5)
    ap.add_argument("--out", required=True)
    ap.add_argument("--allow-partial", action="store_true", help="Explicitly write a marked incomplete snapshot")
    args = ap.parse_args()
    try:
        if date.fromisoformat(args.since)>date.fromisoformat(args.until):
            raise ValueError("Reversed observation window")
        if not 1<=args.per_page<=100 or not 1<=args.max_pages<=10:
            raise ValueError("Pagination must be 1..100 items and 1..10 pages")
        import re
        if not all(re.fullmatch(r"[A-Za-z0-9_.-]+", v) for v in [args.owner,args.repo]):
            raise ValueError("Invalid repository identity")
    except ValueError as error:
        ap.error(str(error))
    query = build_query(args.owner,args.repo,args.since,args.until,args.query)
    result = collect(query,args.per_page,args.max_pages,args.sort,args.order,os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN"))
    result.update(owner=args.owner,repo=args.repo,since=args.since,until=args.until,sort=args.sort,order=args.order)
    if not result["complete"]:
        print("Incomplete refresh: " + "; ".join(result["problems"]),file=sys.stderr)
        if not args.allow_partial:
            return 2  # Preserve previous successful artifact.
    atomic_text(args.out,json.dumps(result,indent=2)+"\n")
    print(f"Wrote {result['fetched_count']} unique issues; complete={result['complete']}",file=sys.stderr)
    return 0

if __name__ == "__main__":
    sys.exit(main())
