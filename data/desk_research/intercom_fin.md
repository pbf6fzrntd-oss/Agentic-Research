# Desk research notes — Intercom Fin

Customer-support domain has no reachable GitHub issue tracker or forum
(Reddit/HN blocked, `community.intercom.com` and `g2.com` blocked — see
spec's Sourcing table). All evidence below is from WebSearch-reachable
analyst/review/comparison content, each independently authored and cited
with its URL in `data/findings.csv`. This file is the readable version of
those same rows; the CSV is the source of truth for scoring.

## Why Fin, not Decagon/Sierra/Chatwoot Captain

See `AGENT_GAPS_RESEARCH_SPEC.md` § "Customer-support product pick" for the
full rationale. Short version: Chatwoot Captain would have matched the
GitHub-mining method used for the other two domains, but a targeted search
turned up zero in-window Captain-specific issues in an otherwise-active
repo — there wasn't a real dataset there. Fin has the richest *independent*
public evidence trail of the closed products.

## Findings

### Resolution rate is inflated and internally inconsistent (CS-RESRATE)

- Independent tests put real-world resolution rates at 38-72%, against an
  advertised 76% average. ([sitegpt.ai](https://sitegpt.ai/blog/intercom-fin-ai-review))
- "3 Failure Modes Behind the 45-53% Production Rate" — a rate well below
  the guarantee-page figure. ([clonedesk.ai](https://clonedesk.ai/blog/intercom-fin-limitations))
- Fin's own pages disagree with each other: 76% on the guarantee page vs.
  71% across 7,000+ customers on the Sierra-comparison page, both live in
  August 2026. ([getcor.ai](https://getcor.ai/blog/reviews/fin))
- A controlled Vanta evaluation had Fin resolving 73% of tickets vs.
  Decagon's 49% in the same test — resolution rate depends heavily on which
  tickets are counted and whether a handoff counts as a failure, which is
  exactly why the headline number is contested.
  ([superkind.ai](https://superkind.ai/blog/ai-customer-support-agents))

### Pricing is unpredictable and runs over the advertised figure (CS-PRICING)

- Final bills land 2-5x higher than the pricing page implies once seats,
  the $0.99/resolution AI fee, and add-ons combine.
  ([sitegpt.ai](https://sitegpt.ai/blog/intercom-fin-ai-review))
- Per-resolution billing charges for "assumed-resolved" conversations where
  the customer simply went quiet, not a confirmed resolution.
  ([getmacha.com](https://www.getmacha.com/blog/intercom-fin-ai-agent-complete-guide))
- Pricing scales unpredictably as the agent improves/handles more volume,
  complicating cost forecasting.
  ([myaskai.com](https://myaskai.com/blog/intercom-fin-ai-agent-complete-guide-2026))
- Named as the single most common reason evaluated teams look at
  alternatives, despite otherwise-strong capability/setup sentiment.
  ([inkeep.com](https://inkeep.com/blog/inkeep-vs-intercom-fin-ai))

### No multi-agent orchestration (CS-NOORCHESTRATION)

- An exhaustive audit across 11 documentation sources / 31 URLs of
  Intercom's own 2026 docs found no evidence of multi-agent orchestration,
  agent-to-agent communication, specialist routing, or delegation patterns.
  Fin also cannot book or confirm meetings.
  ([clonedesk.ai](https://clonedesk.ai/blog/intercom-fin-limitations))
- Kept at low response_rate (1) deliberately — see spec's disqualifier
  guidance — but strategically significant because it's the same
  orchestration-immaturity theme independently found in the coding domain
  (`CODE-SUBAGENT`).

### Decision explainability gap (CS-EXPLAINABILITY)

- Raised as a category-level weakness ("hard to see why the agent made a
  particular decision") in reviews that directly benchmark Decagon against
  Fin and Sierra. Decagon's "Trace View" feature exists specifically to
  answer this. ([eesel.ai](https://www.eesel.ai/blog/decagon-ai-review),
  [mavenagi.com](https://www.mavenagi.com/blog/decagon-reviews))
- Comparison-sourced rather than a direct Fin complaint thread — weighted
  down accordingly (see findings.csv notes).

### Deployment rigidity (CS-DEPLOYRIGID)

- Cloud-only with regional options (US/EU/AU); no self-hosted, on-premise,
  or air-gapped deployment — a hard blocker for some regulated-industry
  buyers. ([clonedesk.ai](https://clonedesk.ai/blog/intercom-fin-limitations))
- Single source, kept at low response_rate deliberately.
