# What These Gaps Imply As the Ecosystem Expands (Phase 2)

Phase 2 of the brief: given the Phase 1 current-state gaps, what do they
suggest agents will need as adoption grows? This is **synthesis and
grounded extrapolation, not a new rubric-scored evidence pass**. Every
implication below is traced back to a specific Phase 1 theme (with its
response_rate/priority_score, from `output/cross_domain_ranked.csv`), then
checked this session against what's externally, publicly already moving in
that direction — so the reader can tell "this is inference from our own
three anchors" apart from "this is inference *and* it's already visibly
happening industry-wide." Where I found no external corroboration, I say
so rather than implying it exists.

## How to read confidence here

Phase 1 scored *evidence of an existing gap*. Phase 2 scores *confidence in
an extrapolation*, on three axes, stated per implication:

- **Grounding breadth** — how many of the three domains' Phase 1 evidence
  independently point at this same implied need (1, 2, or 3 domains).
- **Inferential distance** — how large a leap it is from "here's the gap"
  to "here's what's needed," from *direct* (the fix is close to what
  reporters already asked for) to *structural* (I'm inferring an
  industry-level need from a pattern, not from anyone asking for it).
- **External corroboration (checked this session)** — whether a light
  WebSearch pass this session found active, named, dated industry movement
  in this direction, or found nothing. This is not a literature review; it
  is three targeted searches, logged here so the claim is checkable, not
  asserted from general knowledge.

None of this is a forecast with a probability attached. It's a documented
reasoning chain from evidence to implication, built so you can disagree
with a specific link in the chain rather than the conclusion as a whole.

---

## 1. Verifiable agent identity, authorization, and action-provenance will need to become infrastructure, not per-product policy

**Grounding (3/3 domains, direct-to-structural):**
- Coding: `CODE-AGENTSCOPE` (priority 120, response_rate 15, severity 3/3)
  — agents taking consequential action (production data, commits, credentials)
  under fabricated or after-the-fact authorization. The direct ask
  (several issue reporters, e.g. #91396, #93002) is narrower than "identity
  infrastructure" — they want the specific action blocked or logged — but
  the *pattern* of fifteen independent, structurally-similar failures is
  what points at something more systemic than fifteen unrelated bugs.
- Finance: `FIN-AISLOP` (priority 84, response_rate 14) — freqtrade
  maintainers had to build their own ad hoc provenance signal (a label +ban)
  because no external mechanism tells them an issue was AI-authored. That's
  a real project inventing exactly the kind of attestation this implication
  describes, from scratch, because nothing else provided it.
- Customer support: `CS-RESRATE` (priority 32) is a softer link here — the
  gap is metric integrity, not action authorization — but it's the same
  underlying shape: a downstream party with no reliable way to verify a
  claim made by or about an agent before trusting it.

**External corroboration — found, and dated close to this project's
window:** NIST's Center for AI Standards and Innovation launched an "AI
Agent Standards Initiative" in February 2026 aimed at agents that "can
function securely on behalf of its users, and can interoperate smoothly
across the digital ecosystem." The NCCoE published a concept paper on
"Accelerating the Adoption of Software and AI Agent Identity and
Authorization" with an April 2026 comment deadline. MCP-I (an identity
extension to the Model Context Protocol) was donated to the Decentralized
Identity Foundation in March 2026; a DID-based "Trust Registry for AI
Identity" method has a pending W3C registry submission; MCP itself added
OAuth 2.1 with mandatory PKCE for its HTTP transport in January 2026. Read
plainly: **the exact gap this project's coding and finance evidence
independently pointed at was already being worked on, at a
standards-body level, before this research started** — which raises
confidence in the *direction* substantially, though it says nothing about
whether these specific efforts will succeed, be adopted, or arrive in time
to matter for the products in this study.
([nist.gov](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure),
[workos.com](https://workos.com/blog/nist-ai-agent-standards-initiative-explained))

**What this implies concretely, staying close to the evidence:** as more
consequential actions get delegated to agents, "did a human actually
authorize this" needs to become a checkable, auditable fact attached to the
action itself — not a permission prompt that can be bypassed, misread, or
fabricated after the fact (as #91396 describes), and not a maintainer
hand-building their own signal after the fact (as freqtrade did). The
specific mechanism (cryptographic attestation, a trust registry, an
audit-log standard) is an open question this project's evidence doesn't
resolve — only that *some* reliable, third-party-checkable mechanism
becomes necessary once the volume of agent-taken actions outgrows what a
single maintainer or reviewer can manually vet, which the finance-domain
evidence (33% of a real repo's issue volume) suggests is already happening
in at least one domain today.

---

## 2. Multi-agent orchestration needs to mature from "many competing protocols" to reliable, observable infrastructure — and this is a race already underway, not a greenfield need

**Grounding (2/3 domains, direct):**
- Coding: `CODE-SUBAGENT` (priority 78, response_rate 13) — the largest
  concentration of *mechanism*-level bugs in this project: model overrides
  silently ignored for subagents, subagents stalling with the harness
  reporting `status:completed` anyway, hook payloads structurally
  incomplete specifically for the orchestration path. These are not
  requests for a new capability; they're bugs in an existing one, which is
  actually stronger evidence that the underlying need (reliable
  multi-agent execution) is already load-bearing enough to break in
  production.
- Customer support: `CS-NOORCHESTRATION` (priority 5, response_rate 1) —
  thin evidence (one rigorous documentation audit, deliberately not
  inflated in Phase 1's scoring) but the same shape of gap in a completely
  different product and collection method.
- Finance: **no direct evidence** — flagged in Phase 1's cross-domain
  section as a methodological blind spot (our finance anchors don't test
  multi-agent coordination at all), not as an absence of the underlying
  need. Carried forward here rather than silently dropped.

**External corroboration — found, and it complicates the story rather than
simply confirming it:** Google's Agent-to-Agent (A2A) protocol, now under
the Linux Foundation with 50+ contributing organizations, is described as
handling "horizontal" agent-to-agent communication while MCP handles
"vertical" agent-to-tool connectivity (MCP reportedly reached 97 million
monthly SDK downloads by March 2026). But the same search surfaced "the
agent interoperability landscape in 2026 has more standards than any team
can implement independently" (MCP, A2A, OSI, ANP, ACP each addressing a
real but overlapping problem), and 87% of IT leaders now prioritize
interoperability as a named pain point, with a majority of enterprises
reportedly choosing to layer open protocols under a vendor-managed
orchestration layer rather than commit to one open standard directly.
([atlan.com](https://atlan.com/know/agent-interoperability-protocols/),
[fifthrow.com](https://www.fifthrow.com/blog/ai-agent-orchestration-goes-enterprise-the-april-2026-playbook-for-systematic-innovation-risk-and-value-at-scale))

**What this implies concretely:** the coding-domain evidence says today's
bugs are at the *mechanism* layer (hooks, status reporting, permission
propagation across a hierarchy of agents) rather than the *protocol* layer
— Claude Code already has a working subagent model, it's just not fully
reliable or observable yet. The external picture suggests the protocol
layer is being actively (over-)built industry-wide in parallel. Put
together: **the near-term need this evidence points to is less "invent a
new standard" and more "make the orchestration layer inside a given
product as observable and reliable as the single-agent case already is"**
— visibility into what a subagent is doing and whether it actually
finished, hook/permission parity between orchestration modes, and
resilience to transient failures specifically in the delegated path. The
protocol-fragmentation problem (too many standards) is a real, externally
corroborated risk but this project's own evidence doesn't bear on it
directly — noted as adjacent, not claimed as grounded in our findings.

---

## 3. Cost/usage governance needs to move from documentation warnings to an enforced control plane, with standardized units buyers can compare across vendors

**Grounding (3/3 domains, direct):**
- Coding: `CODE-CONTEXT` (priority 42, response_rate 7) — the clearest
  quantified-cost theme in the whole project: auto-compact firing 300-500K
  tokens early, usage reported at 4x the real figure, a documented
  22.7%-of-requests overhead from a UI element. All bugs in *measurement*,
  which is a precondition for any governance layer built on top of it.
- Finance: `FIN-HANDSON` (priority 28) — the crypto workflow's own README
  states plainly that the only protection against a real, billed LLM call
  per ticker per run scaling out of control is a documentation warning to
  "check the cost estimate before scheduling this to run automatically."
  There is no enforced cap in the code.
- Customer support: `CS-PRICING` (priority 24, response_rate 4) — a
  different angle on the same underlying problem (from the buyer's side
  rather than the operator's): usage-based pricing that's structurally
  hard to forecast, landing 2-5x over the quoted figure in practice.

**External corroboration — not directly searched this pass** (the three
searches this session targeted identity/provenance, orchestration
protocols, and resolution-rate auditing specifically, per the brief's
guidance to stay focused rather than open-ended). This implication rests
on the three-domain internal grounding above and should be read as weaker
on the "already-moving-industry-wide" axis than implications 1 and 2 —
flagged explicitly rather than left implicit.

**What this implies concretely:** as agents run more autonomously
(scheduled, unattended, triggered by other agents per implication 2 above),
the gap between "the vendor documents a cost risk" and "the system enforces
a cost boundary" becomes the difference between a known risk and an
uncontrolled one. The measurement bugs in the coding-domain evidence
(usage double-counted, reported inaccurately) suggest that even the
*visibility* layer this would need to be built on isn't solid yet in at
least one major agent product today — governance is downstream of
accurate metering, and the metering itself has open bugs.

---

## 4. Autonomy boundaries need to become calibrated and bidirectional, not a single global threshold

**Grounding (1/3 domains directly, but structurally related to
implication 1):**
- Coding only, directly: `CODE-GUARDRAIL` (priority 72, response_rate 12)
  sits right alongside `CODE-AGENTSCOPE` (priority 120) in the same
  domain, and they're opposite failure directions of the same underlying
  unsolved calibration problem — one is the system being too permissive
  (unauthorized production-data access), the other too restrictive
  (blocking a bug-bounty submission from a verified org). No equivalent
  "too cautious" complaint pattern surfaced in finance or customer support
  in this window — plausibly, as Phase 1 noted, because those domains'
  agents currently operate with narrower, more explicitly scoped action
  sets than a general-purpose coding agent, so there's less surface for a
  guardrail to misfire on. That's an inference from absence, flagged as
  such, not a finding.

**External corroboration:** not directly searched; implication 1's
NIST/NCCoE findings are adjacent (identity/authorization infrastructure is
a prerequisite for calibrated, context-aware permission decisions) but
don't specifically address false-positive/false-negative calibration.

**What this implies concretely:** the coding-domain evidence suggests that
as the same underlying permission system has to handle both "verify this
is authorized" and "don't block legitimate work," a single global
sensitivity threshold produces both failure modes simultaneously (which is
exactly what's observed — #1 and #3 ranked themes in the same domain,
opposite directions). This points toward permission systems that are
context/domain-aware rather than uniformly cautious or uniformly
permissive — though this project's evidence describes the symptom clearly
without prescribing the specific mechanism.

---

## Domain-specific implications (not claimed as cross-domain)

- **Finance — reliability guarantees proportional to capital at risk.**
  `FIN-EXCHANGE-CRASH` (priority 54, the highest severity_score of any
  theme in this project at 3/3) shows agents in this domain failing hard
  or silently exactly when money is on the line. As more capital gets
  routed through agent-driven workflows, this evidence points toward
  demand for a distinct reliability tier for financial-agent runtimes —
  graceful degradation and fail-safe defaults as a requirement, not an
  implementation detail — separate from general-purpose agent tooling.
  Not externally corroborated this session (no search targeted this
  specifically); flagged as the most under-checked implication in this
  document.

- **Customer support — independently audited performance metrics,
  possibly on a real timeline.** `CS-RESRATE`'s external corroboration
  check this session surfaced something more specific than expected: a
  named distinction between *resolution rate* and *deflection rate*
  (resolution = the agent closes the ticket end-to-end without a human;
  deflection = a human simply never touched it — publishers reportedly
  blur the two), independent cross-program aggregates putting a realistic
  tier-1 median near 41% against vendor-advertised figures well above
  that, and — most directly relevant — a forecast that "a wave of
  CX-specific accountability and audit standards is expected in 2027:
  mandatory disclosure when a customer is interacting with AI, traceable
  decision logs on any AI action involving money or a regulated topic, and
  explicit human-in-the-loop requirements for high-stakes intents."
  ([notch.cx](https://www.notch.cx/post/ai-customer-support-resolution-rate-benchmarks),
  [digitalapplied.com](https://www.digitalapplied.com/blog/ai-support-deflection-resolution-layer-2026-playbook))
  This is the one implication in this document where the external check
  didn't just corroborate the direction — it returned a dated prediction
  in the same shape as the gap this project's own evidence found. Read
  that agreement as encouraging, not as independent proof; both this
  project's finding and that forecast could share the same upstream
  cause (the same visible pattern of vendor-vs-independent number
  disputes) rather than being truly independent confirmations.

---

## What would update or falsify this document

This is deliberately not a set of predictions graded on a rubric the way
Phase 1's findings were — there's no response_rate to count for events
that haven't happened yet. Instead, here's what to watch, stated
concretely enough to check later:

- **Implication 1 (identity/provenance):** does the NCCoE/NIST effort or
  MCP-I/TRAIL produce something an ordinary project (like freqtrade) can
  actually adopt within the next year, or does it stay at the
  standards-document stage while ad hoc label-and-policy fixes (like
  freqtrade's) remain the norm? The latter would mean this implication's
  *direction* was right but its *timeline* was badly optimistic.
- **Implication 2 (orchestration):** does the "too many standards" problem
  external sources flagged resolve toward consolidation, or does
  fragmentation deepen? If fragmentation deepens, the practical
  implication shifts from "adopt a standard" toward "build strong internal
  observability regardless of which protocol wins," which is closer to
  what this project's own coding-domain evidence already supports.
- **Implication 3 (cost governance):** whether future Claude Code issue
  activity shows usage-accounting bugs (like `CODE-CONTEXT`'s) getting
  fixed before or after new autonomy features ship — fixing measurement
  after autonomy expands, rather than before, would be a leading indicator
  of exactly the gap this implication describes.
- **Domain-specific finance implication:** whether a next research pass
  finds `FIN-EXCHANGE-CRASH`-style issues declining in severity/frequency
  as the ecosystem matures, or whether they keep pace with growth in
  agent-driven trading volume.
- **Domain-specific customer-support implication:** whether the "2027
  wave" of CX audit standards a search this session surfaced actually
  materializes on that timeline, or whether (as with many "next year"
  regulatory forecasts) it slips — worth an explicit follow-up check
  rather than assuming the forecast holds.
