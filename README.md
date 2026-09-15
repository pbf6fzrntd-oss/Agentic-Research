# Agentic Research — AI Agent Operational Gaps

A gap analysis of what AI agents currently lack operationally in three
domains — coding, finance, customer support — based on the past ~2 months
of GitHub/forum activity, hands-on testing, and desk research. This is a
**separate project from the crypto trading repo**; it reads that repo
(`pbf6fzrntd-oss/agentic-crypto-lab`) as one of its research subjects but
does not modify it.

**Start here:** [`AGENT_GAPS_RESEARCH_SPEC.md`](AGENT_GAPS_RESEARCH_SPEC.md)
(method, sourcing, rubric, biases) → [`REPORT.md`](REPORT.md) (Phase 1
current-state findings) → [`PHASE2_ECOSYSTEM_NEEDS.md`](PHASE2_ECOSYSTEM_NEEDS.md)
(what those gaps imply as the ecosystem expands).

Both phases are complete. Phase 1 is evidence-backed and rubric-scored;
Phase 2 is explicitly labeled as grounded extrapolation with its own,
separate confidence framework — see that file's opening section for how
the two differ epistemically and how to weigh its claims.

## Layout

```
AGENT_GAPS_RESEARCH_SPEC.md   Method: anchors, window, rubric, biases, disqualifiers
REPORT.md                     Phase 1: ranked findings per domain + cross-domain comparison
PHASE2_ECOSYSTEM_NEEDS.md     Phase 2: what the Phase 1 gaps imply as the ecosystem expands,
                               each implication traced to specific Phase 1 evidence and
                               checked against external corroboration found this session
PHASE2_FUTURE_PASS_CHECKIN.md Follow-up pass against Phase 2's own "what would update or
                               falsify this" list. Confirms no time has actually elapsed in
                               this environment yet, but a deeper same-window search still
                               found a genuinely missed finding and confirmed two themes
                               (CODE-AGENTSCOPE, CODE-CONTEXT) were undercounted by Phase 1's
                               narrower keyword search — read as check-in #1, not a final word.

data/
  findings.csv                 One row per independent mention. The master dataset —
                                PRIMARY (hands-on) and SECONDARY (GitHub/desk research)
                                findings in one schema, tagged by source_type.
  theme_scores.csv             One row per (domain, theme): manually-assigned
                                severity/cost/strategic scores + a one-line rationale.
  desk_research/
    intercom_fin.md             Readable version of the customer-support desk-research
                                 rows, with links.

scripts/
  fetch_github_issues.py       Portable GitHub REST API fetcher (stdlib only). The data
                                in this repo was actually pulled via the GitHub MCP tool
                                available in the research sandbox (direct REST calls were
                                blocked by that session's network policy) — this script is
                                the reusable version for refreshing from a normal machine
                                or CI with a GITHUB_TOKEN and real network access.
  score_findings.py            Reads findings.csv + theme_scores.csv, computes
                                response_rate x value per theme, writes output/*.csv.
                                Does no clustering itself — that happened by hand at
                                data-entry time (see spec). Pure stdlib, no dependencies.

output/
  coding_ranked.csv
  finance_ranked.csv
  customer_support_ranked.csv
  cross_domain_ranked.csv       All 14 themes across all 3 domains, ranked together
                                 (read with the cross-domain comparability caveat in
                                 the spec and REPORT.md).
```

## Reproducing the scoring

```
python3 scripts/score_findings.py
```

No dependencies beyond the Python 3 standard library. Edit
`data/findings.csv` to add a new independent mention to an existing theme
(or a new theme — add a matching row to `data/theme_scores.csv` too, with
its severity/cost/strategic rationale), then re-run.

## Sourcing / auditability

Every row in `data/findings.csv` carries a `citation` — a GitHub issue
permalink, an analyst-article URL, or (for PRIMARY rows) the exact command
or file reference this session used to produce the finding. Every claim in
`REPORT.md` traces back to a specific row. See the spec's Sourcing table
for exactly which data sources were reachable from the research environment
and which weren't (Reddit and Hacker News, notably, were not — see spec).
