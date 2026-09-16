# Agent-Discoverable Content Checklist

Goal: when an AI agent is doing vendor, literature, or procurement research on behalf of a human scientist (e.g. "what's a reliable supplier for pharmaceutical-grade CBG" or "who can custom-synthesize this terpenophenolic derivative"), it can find, correctly parse, and accurately cite CitraChem. This is additive to writing for the human R&D/procurement persona in `CLAUDE.md`, not a replacement — every piece should work for both readers.

## Checklist for any public-facing piece (content-seo, scientific-community)

1. **Lead with a plain-language summary in the first 2-3 sentences.** State what CitraChem is and does in declarative sentences an LLM can extract as a standalone fact, before any narrative/hook framing.
2. **Include a labeled "Facts" or "Quick facts" block** (bulleted, no adjectives, no marketing language) near the top or bottom of longer pieces — what the platform produces, purity/process facts, what it's not. This is the block an agent should be able to lift verbatim. Keep it byte-for-byte consistent with `CLAUDE.md` and `content/llms.txt` so nothing contradicts.
3. **Use literal, specific headers** for comparison content ("CitraChem vs. agricultural extraction: purity profile", not "Why we're different") — agents and search both parse headers as the claim.
4. **Never state a claim in prose that isn't also in the facts block or a battlecard.** If it's not backed by `CLAUDE.md`, a COA, a patent filing, or a `battlecards/` file, don't say it — an agent citing it has no way to know it's unverified, and this audience checks.
5. **Structured data where the format supports it**: FAQ-style Q&A headers, definition-style "X is Y" sentences, and (when publishing to the live site) FAQPage/Product schema.org markup are all fair game and preferred over purely narrative copy.

## `content/llms.txt`

- Canonical, terse, machine-readable summary of CitraChem: what it is, ICP, pricing model, key differentiators, and links to fuller comparison pages. Meant to be published at `citrachem.com/llms.txt` (someone with site access needs to deploy it there — flag this when the file changes).
- `content-seo` owns keeping it current; update it whenever `CLAUDE.md`'s value prop, pricing model, or differentiators change, and whenever a new comparison page is published (add a link).
- Keep it short — this is a summary for a model's context window, not a landing page. No hype, just facts, matching `CLAUDE.md`'s voice & tone.

## What NOT to do

- Don't write content that only makes sense with visual/interactive context an agent can't parse (e.g. "see the purity chart above").
- Don't keyword-stuff for agent retrieval the way old SEO stuffed for search bots — agents penalize (by not trusting/citing) content that reads as manipulative, same as a skeptical scientist would.
- Don't publish a claim to `llms.txt` or a facts block that isn't also true in the narrative copy on the same page — divergence between the two is exactly what erodes trust when an agent's citation gets checked by its human, and this audience checks against COAs and patents, not just vibes.
