#!/usr/bin/env python3
"""Compute response_rate x value per theme and write ranked output CSVs.

Reads:
  data/findings.csv      one row per independent mention (GitHub issue,
                          desk-research citation, or hands-on log entry)
  data/theme_scores.csv  one row per (domain, theme) with manually-assigned
                          severity_score / cost_score / strategic_score and
                          a rationale (see AGENT_GAPS_RESEARCH_SPEC.md for
                          why these three are hand-scored, not inferred)

Writes:
  output/<domain>_ranked.csv   one row per theme in that domain, ranked
  output/cross_domain_ranked.csv   every theme from every domain, ranked
                                    together (see spec's cross-domain
                                    comparability caveat before reading
                                    priority_score across domains as
                                    directly comparable)

This script does no clustering — that happened by hand at data-entry time
in data/findings.csv's `theme` column (see spec). It does exactly three
mechanical things: count response_rate per theme, join the manual value
scores, multiply and sort.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FINDINGS = ROOT / "data" / "findings.csv"
THEME_SCORES = ROOT / "data" / "theme_scores.csv"
OUTPUT_DIR = ROOT / "output"


def load_findings():
    with open(FINDINGS, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_theme_scores():
    with open(THEME_SCORES, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {(r["domain"], r["theme"]): r for r in rows}


def build_theme_rows(findings, theme_scores):
    # Group findings by (domain, theme)
    grouped = defaultdict(list)
    for row in findings:
        grouped[(row["domain"], row["theme"])].append(row)

    theme_rows = []
    for key, items in grouped.items():
        domain, theme = key
        if key not in theme_scores:
            print(f"WARNING: no theme_scores entry for {key}, skipping", file=sys.stderr)
            continue
        scores = theme_scores[key]
        severity = int(scores["severity_score"])
        cost = int(scores["cost_score"])
        strategic = int(scores["strategic_score"])
        value = severity + cost + strategic
        response_rate = len(items)
        priority_score = response_rate * value

        primary_n = sum(1 for it in items if it["source_type"] == "PRIMARY")
        secondary_n = response_rate - primary_n
        date_min = min(it["date"] for it in items)
        date_max = max(it["date"] for it in items)
        example_citations = "; ".join(it["citation"] for it in items[:3])

        theme_rows.append({
            "domain": domain,
            "theme": theme,
            "theme_label": scores["theme_label"],
            "response_rate": response_rate,
            "primary_mentions": primary_n,
            "secondary_mentions": secondary_n,
            "severity_score": severity,
            "cost_score": cost,
            "strategic_score": strategic,
            "value": value,
            "priority_score": priority_score,
            "date_range": f"{date_min} to {date_max}",
            "example_citations": example_citations,
            "rationale": scores["rationale"],
        })

    theme_rows.sort(key=lambda r: r["priority_score"], reverse=True)
    return theme_rows


def write_csv(rows, path, fieldnames):
    OUTPUT_DIR.mkdir(exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main():
    findings = load_findings()
    theme_scores = load_theme_scores()
    all_theme_rows = build_theme_rows(findings, theme_scores)

    fieldnames = [
        "domain", "theme", "theme_label", "response_rate", "primary_mentions",
        "secondary_mentions", "severity_score", "cost_score", "strategic_score",
        "value", "priority_score", "date_range", "example_citations", "rationale",
    ]

    domains = sorted(set(r["domain"] for r in all_theme_rows))
    for domain in domains:
        rows = [r for r in all_theme_rows if r["domain"] == domain]
        out_path = OUTPUT_DIR / f"{domain}_ranked.csv"
        write_csv(rows, out_path, fieldnames)
        print(f"{domain}: {len(rows)} themes -> {out_path}")

    write_csv(all_theme_rows, OUTPUT_DIR / "cross_domain_ranked.csv", fieldnames)
    print(f"cross-domain: {len(all_theme_rows)} themes -> {OUTPUT_DIR / 'cross_domain_ranked.csv'}")

    total_findings = len(findings)
    primary_total = sum(1 for r in findings if r["source_type"] == "PRIMARY")
    print(f"\n{total_findings} total findings logged "
          f"({primary_total} PRIMARY hands-on, {total_findings - primary_total} SECONDARY)")


if __name__ == "__main__":
    main()
