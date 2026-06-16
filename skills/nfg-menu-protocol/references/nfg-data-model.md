# NFG data model — reference

The target shape for `06_nfg_output.md`. NFG is a structured standard for what a
dish *means*. Every dish record has two complementary halves that are both
load-bearing — never collapse one into the other:

- **Machine Semantics** — strictly enumerated, machine-readable: ingredients,
  cooking methods, allergens, dietary/religious restrictions, taste profile,
  calorie range.
- **Human Narrative** — deliberately free text: story, cultural context, serving
  suggestions, seasonal notes.

## The 8 masters

| Master | Size | Notes |
|---|---|---|
| Store basic info | per store | business type, hours, contact |
| **Dish master** | per store | the core: dish ↔ ingredient_ids ↔ method_ids, price, `verified` flag |
| **Ingredients** | 185 canonical | 3-tier: simple / composite (`is_composite` + `components`) / 18 processed foods. Each carries `allergen_flag` + `restriction_flag` |
| Cooking methods | 20 | grill / fry / boil / steam / raw / pickle / smoke / roast categories |
| Dietary & religious restrictions | 12 | see list below; API-facing, not shown raw in UI |
| **Allergens** | 32 items | mapped per jurisdiction JP / US / EU / CA / AU |
| Taste profiles | 15 | basic 5 (incl. umami) + texture / impression / combined. Numeric `taste_values` never shown raw — the AI verbalizes them |
| Calorie ranges | 5 | coarse ranges, not fake precision |

## Ingredient model (Stage 02 maps onto this)

Three tiers:
- **Simple** — e.g. rice, egg, soy sauce.
- **Composite** — `is_composite: true` with a `components` list. Curry roux →
  flour + fat + beef + dairy. **Always expand composites**, because allergens hide
  inside them.
- **Processed** (18 of them) — manufactured items treated as units.

Each ingredient carries an `allergen_flag` and a `restriction_flag`. **Allergens and
restrictions are derived from ingredients**, not tagged ad hoc on the dish.

## Allergens — 32 items, 5-country mapping

Derive these in Stage 03 by walking the ingredient list. Each allergen maps to a
status per jurisdiction: **mandatory / recommended / none**.

- The 5 jurisdictions are **JP / US / EU / CA / AU**.
- JP-specific items include buckwheat (そば), abalone, salmon roe, matsutake, yam,
  and others; EU-specific include celery, mustard, sulphites, and lupin. They
  coexist in the same 32-item set — this 5-country mapping is itself a
  differentiator, so don't flatten it to a single country.
- Represent each derived allergen as: `allergen — from <ingredient> — [provenance·conf] — JP:<status> US:<status> EU:<status> CA:<status> AU:<status>`.

**Hard-won allergen rules (each one was a real incident):**
- `gelatin` is its own token. It is **not** a meat allergen.
- Pork-free / halal is a **restriction layer**, not an allergen. Don't file it under
  allergens.
- Watch the dessert class of errors — desserts were once mass-mistagged with
  beef + pork. A derived allergen must trace to an actual ingredient.
- A derived allergen inherits the **weakest provenance** in its chain. If any
  ingredient in the chain is `[INFERRED]` or `[UNKNOWN]`, the allergen status is
  not a fact — it is a gap question.

## Dietary & religious restrictions — 12

halal, kosher, hindu, vegan, vegetarian, pescatarian, gluten-free, no-alcohol,
no-pork, no-beef, dairy-free. (That's 11 named in the source; treat the set as the
canonical 12-item master and flag if a 12th applies.) These are API-facing and
derived from ingredients, same as allergens.

## Trust metadata (what makes NFG more than a menu DB)

- **VAD (Verified Authentic Data)** — owner-confirmed data. The product's whole
  claim is "not AI guesses; first-hand verified truth." In this protocol, VAD =
  the `[OPERATOR]` provenance tag.
- **`verification_rank` S / A / B / C** — per-record trust grade. State current
  confidence honestly; don't wait for perfection. For an AI agent this answers
  "can I present this to a user as fact?"
- **`field_confidence`** — per-field AI-vs-verified granularity. In this protocol,
  the inline `[TAG·conf]` on each field *is* the field_confidence.
- **`data_source`** — `live` (paying/real stores) / `corpus` (~1,300
  Google-API-imported stores, `user_id = 19`) / `test`. **Iron rule: write
  operations target `live` only.** Never operate on corpus data as if it were a
  customer.

## Canonical assets — apply in Stage 02, they override inference

These are the hallucination kill-switches. When a menu item matches a canonical
entry, canonical data **overrides** anything the model would generate.

**product_master.json — 244 verified beverage/product entries.** Sake, shochu,
wine, etc., each verified against the maker's official spec. Matching gotcha: never
match by brand-name substring (龍 ⊂ 黒龍 caused brand cross-contamination). Match the
full product identity.

**ingredient_glossary.json — 481 canonical ingredient translations.** English names
are core NFG value, not "just translation" (real failures: カニ面 → "Crab face",
バイ貝 → "buy shell").
- **Policy B (boundary rule):** if a plain English name exists, use it (タイ → Sea
  bream). Use Romaji + gloss **only** for Japan-unique items (へしこ → Heshiko
  (fermented mackerel)).
- Regional accuracy: 若狭牛 → Wakasa Beef (Fukui Wagyu); never apply Fukui labels to
  Ishikawa stores (能登牛 → Noto Beef).

**Food-culture knowledge base — 99 verified dishes** (MAFF regional-cuisine data +
web verification). Cultural narrative comes from this verified dictionary, **not**
from generation — generated "history" hallucinates (GPT once invented an origin
story for sauce katsudon). Discovery can be automated; **inclusion requires
verification.** If a dish isn't in the KB, its cultural narrative is `[INFERRED]`
and should be flagged as such, not presented as established fact.

**Meta-rule for all AI-generated canonical data:** AI generates → human reviews the
diff → apply. Single-shot model output is never trusted wholesale. Draft → diff
review → finalize.

## Taste profiles & calories

- Taste: 15 profiles (basic 5 incl. umami, plus texture / impression / combined).
  Numeric `taste_values` are an inter-subjective description, never shown raw — the
  output should carry both the values and a short verbalization ("rich umami, gentle
  saltiness").
- Calories: 5 coarse ranges. Do not manufacture precise figures; pick a range and
  tag its provenance.
