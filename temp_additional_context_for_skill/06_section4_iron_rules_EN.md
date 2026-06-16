# NFG §4 Operational Iron Rules (excerpt) — safety constraints for the Question Engine

> Excerpt from `matt-handover/06_NFG_SPECIFICATION.md` §4. The constraint layer the Question Engine uses to decide "what to ask / what not to ask" and how to handle safety items.

## Operational iron rules (each one is a scar)

1. **Safety first.** Allergen correctness outranks everything — narrative second, efficiency third. Gelatin is its own token (`gelatin`), *not* a meat allergen; pork-free/halal is a constraint layer, not an allergen.
2. **Allergen changes sync 3 places** — FE `allergens.ts`, BE `agent.py` profile whitelist, `router.py` profile→allergen map. Missing one silently breaks profile injection.
3. **Ground every factual answer in the DB.** No invention.
4. **When the LLM won't comply, move the logic to code.** Prompt-level instructions are the weakest enforcement tier.
5. **"Varies by item" answers must never propagate.** In the kitchen-profile learning loop, an owner answering "depends on the dish" must not cascade to individual menu items. ← **the most important rule for the Question Engine**
6. **Generate once, serve from DB.**
7. **Production data fixes:** count + sample + dry-run + explicit yes, timestamped CSV backup.

## Principles that directly shape Question Engine design (from §5 philosophy)

- **Sincerity (makoto):** menu data must match what's actually served. For safety items, prefer an honest "unknown" over a false "none".
- **Benevolence (jin):** the weakest user (the allergy sufferer) is protected first. Allergen questions must be the most conservative part of the system.
- **Incompleteness as honesty:** ship partial data with explicit confidence rather than fake completeness.
