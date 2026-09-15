# Agent Operational Gaps — Research Spec

**Status:** Phase 1 (current-state gap analysis) — complete, pending review.
Phase 2 (future/expanding-ecosystem implications) is deliberately **not**
started; see "Out of scope for this phase" below.

## The question

What operational gaps currently exist for AI agents in **coding**,
**finance**, and **customer-support** contexts, based on the past ~2 months
of developer forum/GitHub activity for each domain, plus hands-on testing
with Claude Code (coding) and our existing crypto agent workflow (finance),
and desk research on one customer-support agent product? What do those gaps
suggest about what agents will need as the ecosystem expands? *(The second
question is Phase 2 — out of scope here.)*

## The three anchors

| Domain | Anchor | Why |
|---|---|---|
| Coding | **Claude Code** (`anthropics/claude-code` on GitHub) | We can both mine its public issue tracker at full fidelity *and* generate PRIMARY evidence — this research project itself was built using Claude Code, so its own friction is fair game. |
| Finance | **Our existing crypto agent workflow** (`pbf6fzrntd-oss/agentic-crypto-lab`) | Explicitly named in the brief. Attached read-only to this session (see Sourcing below) so hands-on testing is against the real repo, not a simulation. Supplemented with public GitHub activity from `freqtrade/freqtrade`, the largest active open-source algo-trading framework, as a proxy for broader finance-domain developer activity — see bias note below. |
| Customer support | **Intercom Fin** (the "Fin AI Agent") | See pick rationale below. |

### Customer-support product pick: Intercom Fin — rationale

I evaluated Intercom Fin, Decagon, Sierra, and Chatwoot's "Captain" (the one
open-source option with a real public GitHub tracker) before deciding.

- **Chatwoot Captain** was the methodologically tempting choice — full GitHub
  issue-tracker access, same technique as the other two domains. But a
  targeted search of `chatwoot/chatwoot` issues in the window for
  Captain/AI-agent-specific reports returned **zero** results. The repo is
  very active (145 issues in-window) but almost none of that activity is
  about the AI agent feature specifically, so it wouldn't actually answer
  the question asked.
- **Decagon** and **Sierra** are enterprise/private products with thin public
  discussion trails reachable from this environment.
- **Intercom Fin** is the dominant, most-referenced product in the category —
  every comparison article benchmarks against it — and it has a genuinely
  rich, *independent* public trail: multiple analyst/review sites publish
  concrete, checkable numbers (resolution rates, pricing structures,
  documented capability audits), not just marketing copy. That independence
  is exactly what the response_rate side of the rubric needs.

Net: Fin gives the strongest *evidence*, even though gathering it required
desk research (reviews, comparisons, vendor docs) rather than issue-tracker
mining. That method difference is a cross-domain comparability caveat, called
out explicitly below and in the report.

## Evaluation window

**2026-07-15 to 2026-09-15** (the ~2 months preceding this research, run on
2026-09-15). Every finding is timestamped; anything outside this window was
excluded even if discovered while searching (e.g., a March 2026 Reddit
thread about Claude Code quota exhaustion was found and dropped — see
Disqualifiers).

## Sourcing — what's actually reachable from this environment

Tested directly before building anything, not assumed:

| Source | Reachable? | Notes |
|---|---|---|
| GitHub (issues, via the GitHub MCP tools) | **Yes, fully** | This is the highest-fidelity source available: full-text search, sort by comments/reactions/interactions, structured fields, real timestamps. Became the backbone of both the coding and finance datasets. Direct `curl`/REST calls to `api.github.com` are blocked by this session's network policy (403, distinct from GitHub auth) — the MCP tool path is the one that works here. GitHub **Discussions** are not exposed by any available tool (issues only). |
| WebSearch | **Yes** | Returns titles/URLs/snippets, including synthesized summaries of content it can't hand back verbatim. Good for desk research citations; weak for pulling full forum thread text. |
| WebFetch — Reddit, Hacker News (incl. HN Algolia API), G2, `community.intercom.com`, `chatwoot.com` | **No** | All blocked at the network-egress layer (`EGRESS_BLOCKED`), not by the sites themselves. This ruled out building scrapers against any of them — there'd be nothing for the scraper to reach in this environment. |
| WebFetch — generic docs/blog/vendor content | Mixed | Some vendor marketing/community domains are blocked outright (see above); plain articles and docs sites generally are not. Checked case by case rather than assumed. |
| Our crypto agent workflow repo | **Yes** | Attached read-only this session (`add_repo` → clone) specifically so hands-on testing would be against the real thing, per your direction. |

**Conclusion used to scope the tooling:** GitHub issue search is the one
source reachable at full fidelity, so it does the heavy lifting for coding
and finance. Reddit/HN could not be scraped in this environment (egress
blocked), so forum sentiment enters only where WebSearch surfaces it
indirectly (desk research), never as a primary counted source. This is a
property of *this sandbox*, not a permanent limitation — `scripts/fetch_github_issues.py`
is written against the plain GitHub REST API so it also runs unmodified
from a normal machine/CI with network access and a token.

## Scoring rubric

For each **theme** (a cluster of independent mentions of the same
underlying gap — see Clustering below):

```
priority_score = response_rate × value
value = severity_score + cost_score + strategic_score      (each 0–3, so value ∈ [0,9])
```

- **response_rate** — count of independent mentions/threads referencing the
  same underlying issue. Computed mechanically by the scoring script as a
  row count per (domain, theme) in `data/findings.csv`. "Independent" is
  enforced at data-entry time: duplicate-of / same-root-cause issues (e.g.
  GitHub's own "Duplicate" label, or two analyst posts visibly citing the
  same original source) are logged as **one** row, not two — see
  Disqualifiers.
- **severity_score (0–3)** — how strong the severity/blocking language is:
  0 = none, 1 = friction/annoyance, 2 = strong blocking ("unacceptable",
  "no way to work this way"), 3 = fatal/data-loss/funds-at-risk/security
  language present in at least one independent mention.
- **cost_score (0–3)** — whether a time-or-money cost is mentioned: 0 = none,
  1 = minor/indirect, 2 = implied but unquantified (e.g. "burns budget"),
  3 = an explicit dollar figure, resolution-rate delta, or "kills the bot in
  production" cost.
- **strategic_score (0–3)** — researcher judgment of how central the gap is
  to whether agents can be trusted/adopted at scale in that domain: 1 =
  narrow/nice-to-have, 2 = meaningfully important, 3 = foundational (trust
  boundary, core evaluation validity, or a pattern that recurs across
  domains).

severity_score and cost_score are assigned per theme from the balance of
evidence in its mentions (documented per-theme in `data/theme_scores.csv`,
with a one-line rationale each — this is manual, not NLP-inferred, exactly
because grading "how severe" free text is doesn't survive naive keyword
matching cleanly enough to trust unsupervised). response_rate is the one
component computed purely mechanically by the script, precisely because it's
the one component that *should* be a plain count, not a judgment call.

## Clustering / theme-grouping approach

**Manual, semantic theme-tagging — not ML clustering, not pure keyword
matching.** Every raw item (GitHub issue, desk-research citation, hands-on
log entry) was read and assigned one theme by hand in `data/findings.csv`'s
`theme` column. The brief's guidance to keep this simple and avoid ML unless
keyword grouping proves insufficient turned out to cut even further than
expected: with ~110 raw items total, semantic grouping by hand (an
experienced reader recognizing "these are the same underlying gap") was both
faster and more accurate than building a keyword-cluster step — two GitHub
issues about "the agent edited a file it wasn't authorized to touch" don't
reliably share vocabulary. `scripts/score_findings.py` is the mechanical
part: it *counts* rows per theme, joins the manual severity/cost/strategic
scores, multiplies, and sorts. It does no clustering itself; the clustering
already happened at data-entry time. If this project scales to thousands of
raw items, that's exactly the point where a keyword-assisted first pass
becomes worth it — noted as a limitation, not solved preemptively.

## Biases to watch for (and how each is handled here)

1. **Forum activity skews toward vocal power users.** GitHub issue reporters
   are self-selected — people frustrated enough to write a structured bug
   report, not a representative sample of all users. Mitigation: I did not
   scale findings by GitHub star count or account age; I did downweight
   single-line, low-effort duplicate-pattern issues (e.g. a wave of nearly
   identical one-line "stop blocking me" reports) by treating them as one
   *theme* with a high response_rate rather than crediting each with
   independent strategic weight — the theme's value score doesn't multiply
   by how many people typed the same six words.
2. **Two months can catch a temporary spike, not a persistent pattern.**
   Mitigation: where a theme's mentions cluster in a narrow sub-window (e.g.
   all in the first or last two weeks) rather than spread across the full
   ~60 days, that's flagged in the theme's rationale in
   `data/theme_scores.csv`. None of the top-ranked themes in this pass
   turned out to be a narrow spike — each has mentions spread across most
   of the window — but this is checked per theme, not assumed.
3. **Duplicate/bot-amplified issues inflate response_rate.** Mitigation:
   GitHub's own `Duplicate` label and visible "same as #NNNNN" cross-references
   collapse into one row. freqtrade's `AI Slop` label is a special case —
   it is *itself* a finding (see finance domain), not noise to be
   collapsed, because the gap it evidences is "agents produce enough
   low-effort submissions that maintainers built dedicated tooling to
   manage them," and that claim is exactly as strong as the count of
   distinctly-labeled instances.
4. **The three domains' forums have different volumes and cultures, so raw
   cross-domain comparison needs care.** Claude Code's tracker is high-volume
   and immediate (structured bug-report templates, fast triage labels).
   freqtrade is smaller, more terse, and has an explicit anti-AI-issue
   policy that itself shapes what gets reported. Intercom Fin has *no*
   public issue tracker at all — its evidence is desk research, a
   structurally different collection method. **Cross-domain rankings in
   this report compare gap *categories* (is the same kind of gap present in
   multiple domains?), never raw priority_score numbers across domains** —
   a priority_score of 40 in coding and 12 in customer support does not mean
   the coding gap matters 3.3× more; it partly means Claude Code's tracker
   is far larger and faster-moving than Fin's desk-research trail.

## What disqualifies a finding

- **Already solved by an existing, shipped feature** — checked against the
  issue's own thread (a maintainer reply pointing to a shipped fix) or
  current docs before counting it as open.
- **A high score tracing back to a small cluster amplifying itself rather
  than independent occurrences** — e.g., several blog posts that all cite
  the same single original source/benchmark are logged as one independent
  mention, not several. Concretely excluded during this pass:
  - A March 2026 Reddit thread ("20x max usage gone in 19 minutes") surfaced
    while searching Claude Code sentiment — outside the 2-month window,
    dropped.
  - Several near-identical one-line Claude Code issues (e.g. "[FEATURE]"
    with no body, one-word titles) were folded into their theme's count
    only where the *pattern itself* is the finding (guardrail
    false-positives); truly empty/unreadable issues were excluded outright.
  - A cluster of customer-support blog posts making the same "Fin is 2-5x
    more expensive than advertised" claim was checked for independent
    sourcing (different named authors/outlets, not reposts) before being
    counted at response_rate 4, not 4× a single source.
  - Two low-evidence customer-support findings (no self-hosted deployment
    option; no multi-agent orchestration) were *kept* but deliberately
    scored with response_rate 1–2 rather than inflated, specifically
    because only one deep-audit source substantiates each — the rubric is
    allowed to rank something low; it isn't fixed post hoc to look better.

## Hands-on testing log format

One unified table, `data/findings.csv`, with a `source_type` column of
`PRIMARY` (hands-on, from actually operating Claude Code or the crypto
workflow this session) or `SECONDARY` (GitHub issue or desk-research
citation). PRIMARY entries carry the same columns as everything else
(domain, theme, severity/cost signal, date, a citation — for hands-on
entries, the citation is the reproducing command/action taken this session)
so they score on the exact same rubric, not a separate parallel scale. This
was simpler and more auditable than a second log format, and it directly
satisfies "tagged clearly as PRIMARY vs SECONDARY" without a second
schema to keep in sync.

No hands-on log exists for the customer-support domain — I do not have an
Intercom account or Fin deployment to operate, and the brief scopes that
domain as desk research only.

## Out of scope for this phase

No speculation about future/expanding-ecosystem needs. That is Phase 2,
explicitly deferred pending your review of this phase's method and findings.
