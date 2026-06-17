# NFG (Nicomacos Food Graph) — Standard, Data Quality Rules & Why It Matters

> Source context provided by Matt at the start of the skill-building session. This is
> the substantive spec the `nfg-menu-protocol` skill is designed to produce data for.
> Canonical project sources (not in this repo): `ngraph/docs/NFG_data_master.md` (data
> model), `ngraph/docs/NFG_philosophy.md` (design principles), `ngraph/docs/SYSTEM_SPEC.md`
> (operational spec).

## 1. What NFG is

NFG is a structured standard for what a dish *means*, designed so AI agents can
consume food data reliably. Every dish record has two complementary halves:

- **Machine Semantics** — ingredients, cooking methods, allergens, dietary/religious
  constraints, taste profile, calorie range. Strictly enumerated, machine-readable.
- **Human Narrative** — story, cultural context, serving suggestions, seasonal notes.
  Deliberately free-text; the part structure can't capture.

The bet: as AI agents (assistants, booking agents, delivery agents) become how people
choose food, **the data they can trust gets referenced — and referenced data wins**.
NFG aims to be that trust layer ("the JAN code of food"): one verified record, sold
via API to many consuming services (S2S: SaaS-to-Standard).

## 2. The data model (8 masters)

| Master | Size | Notes |
|---|---|---|
| Store basic info | per store | business type, hours, contact |
| **Dish master** | per store | the core: dish ↔ ingredient_ids ↔ method_ids, price, `verified` flag |
| **Ingredients** | 185 canonical | 3-tier: simple / composite (`is_composite` + `components`, e.g. curry roux → flour+fat+beef+dairy) / 18 processed foods. Each carries `allergen_flag` + `restriction_flag` — allergens and dietary constraints are **derived from ingredients**, not tagged ad hoc |
| Cooking methods | 20 | grill/fry/boil/steam/raw/pickle/smoke/roast categories |
| Dietary & religious restrictions | 12 | halal, kosher, hindu, vegan, vegetarian, pescatarian, gluten-free, no-alcohol, no-pork, no-beef, dairy-free — API-facing, not exposed raw in UI |
| **Allergens** | 32 items | mapped per jurisdiction: JP / US / EU / CA / AU, each mandatory/recommended/none. JP-specific items (buckwheat, abalone, salmon roe…) and EU-specific (celery, mustard, sulphites, lupin) coexist — this 5-country mapping is itself a differentiator |
| Taste profiles | 15 | basic 5 (incl. umami) + texture/impression/combined. Numeric `taste_values` are never shown raw to users — the AI verbalizes them ("rich umami, gentle saltiness"). Shared inter-subjective description, not objective measurement |
| Calorie ranges | 5 | coarse ranges, not fake precision |

### Trust metadata (what makes NFG more than a menu DB)

- **VAD (Verified Authentic Data)** — owner-confirmed data. The product's whole claim
  is "not AI guesses; first-hand verified truth."
- **`verification_rank` S/A/B/C** — per-record trust grade. Don't wait for perfection;
  state current confidence honestly. For an AI agent this is machine-readable trust
  metadata: "can I present this to a user as fact?"
- **`field_confidence`** — per-field AI-vs-verified granularity.
- **`data_source`** — `live` (paying/real stores, 10 today) / `corpus` (~1,300
  Google-API-imported stores, `user_id = 19`) / `test`. **Iron rule: bulk write
  operations (allergen backfill, question generation, enrichment) target `live` only.**
  Corpus stores are vocabulary/training material — never operated on as if customers.

## 3. Canonical-data assets and the policies behind them

These took months of incident-driven refinement. The policies matter more than the files.

### product_master.json — 244 verified beverage/product entries
Sake, shochu, wine etc., each verified against the **brewery/maker's official spec**.
When a menu item matches a canonical entry, canonical data **overrides** anything GPT
generates. This is the hallucination kill-switch. Matching gotcha: never match by
brand-name substring (龍 ⊂ 黒龍 caused cross-contamination of brands).

### ingredient_glossary.json — 481 canonical ingredient translations
English ingredient names are core NFG value (real failures: カニ面 → "Crab face",
バイ貝 → "buy shell").
- **Policy B (deterministic boundary rule):** if a plain English name exists, use it
  (タイ → Sea bream); Romaji + gloss **only** for Japan-unique items (へしこ → Heshiko
  (fermented mackerel)).
- Regional accuracy: 若狭牛 → Wakasa Beef (Fukui Wagyu); never apply Fukui labels to
  Ishikawa stores (能登牛 → Noto Beef).

### The meta-rule for ALL AI-generated canonical data
**AI generates → human reviews the diff → apply.** Single-shot GPT output is never
trusted wholesale. Draft → diff review → finalize. Always keep a timestamped backup
before applying.

### Knowledge base discipline
Rich cultural explanations come from a **verified canonical dictionary** (99 dishes,
sourced from MAFF regional-cuisine data + web verification), not from generation.
Generated "history" hallucinates. Discovery can be automated; **inclusion requires
verification**.

## 4. Operational iron rules (each one is a scar)

1. **Safety first.** Allergen correctness outranks everything. Examples: gelatin is its
   own token (`gelatin`), *not* a meat allergen; pork-free/halal is a constraint layer,
   not an allergen; desserts mass-mistagged with beef+pork was a real cleanup.
2. **Allergen changes sync 3 places** — FE `allergens.ts`, BE `agent.py` profile
   whitelist, `router.py` profile→allergen map.
3. **Ground every factual answer in the DB.** Drink lists, pairings, "do you have X" —
   all go through status-filtered tools with "results only, no invention" prompts.
4. **When the LLM won't comply, move the logic to code.** Prompt-level instructions are
   the weakest enforcement tier.
5. **"Varies by item" answers must never propagate.** An owner answering "depends on the
   dish" must not cascade to individual menu items.
6. **Generate once, serve from DB.** NFG enrichment is batch (gpt-4o) → stored; runtime
   reads the DB.
7. **Production data fixes:** count + sample + dry-run + explicit yes before any
   destructive operation; timestamped CSV backup; PITR is the last resort.

## 5. Design principles (philosophy, compressed)

Grounded in 11 principles (Aristotle's *Nicomachean Ethics* gives the company its name):
- **The mean (mesotēs):** between hallucination (excess) and empty fields (deficiency)
  sits verified, confidence-graded data. `verification_rank` is "the mean, made explicit."
- **Sincerity (makoto):** menu data must match what's actually served — the ethical basis
  of VAD.
- **Incompleteness as honesty:** ship partial data with explicit confidence rather than
  fake completeness.
- **Structure + narrative, never one alone.**
- **Benevolence (jin):** the weakest user — the allergy sufferer — is protected first.
- **Agent economy:** agents need machine-readable *trust* (verification_rank,
  field_confidence) as much as machine-readable *data*. Roadmap: JSON-LD / Schema.org /
  FoodOn compatibility, MCP/A2A-ready API, per-query micropricing.

Open-standard intent: Layer 1 (NFG Core Schema) is meant to become an open spec. The
moat isn't hoarding the schema — it's owning the verified data and the verification loop.

## 6. Why this is the business

- A POS menu is for *ordering*; NFG is the *meaning* of the menu.
- Fragmented industry × labor shortage × multilingual demand → restaurants need work
  *done for them* (the wedge that funds data creation).
- Each verified record is created once and can be sold N times via API.
- Defensibility is the **verification loop** (owner confirmation + incident-hardened
  canonicalization pipeline + 5-country allergen mapping), not any single file.
