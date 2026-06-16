# Canonical assets

These are the verified-data "kill switches" that stop the model from inventing
specs. When a menu item matches a canonical entry, **the canonical value overrides
anything the model would generate**, and the field is tagged `[CANONICAL]`.

The files here are **seeds** — a small, real-shaped starter set plus the schema each
asset follows. In production the full assets (244 beverages, 481 glossary terms, 99
food-culture dishes) live in the project / database. If the user points you at a
fuller copy, prefer it over these seeds.

## Files

| File | What it is | Full size (prod) |
|---|---|---|
| `product_master.json` | Verified beverage/product specs | 244 |
| `ingredient_glossary.json` | Verified EN ingredient names + boundary rule | 481 |
| `food_culture_kb.json` | Verified regional-dish narratives | 99 |
| `schemas/*.schema.json` | The shape each asset must follow | — |
| `candidates/` | Draft, **unverified** proposed entries (a human-review queue) | — |

## Lookup order at the start of a run

1. A path the user explicitly gives you (fullest source of truth).
2. A project/repo copy if one exists (e.g. an `nfg/data/` directory).
3. These bundled seeds.

Record which source you used in `01_source_capture.md`.

## Matching rules (these encode real past incidents)

- **product_master:** match on the *full product identity*, never a brand-name
  substring. 龍 is a substring of 黒龍 — matching by substring cross-contaminated
  brands. Require the full name (and maker, where present) to agree.
- **ingredient_glossary — Policy B (boundary rule):** if a plain English name
  exists, use it (タイ → Sea bream). Use Romaji + gloss **only** for Japan-unique
  items (へしこ → Heshiko (fermented mackerel)). Respect regional labels (能登牛 →
  Noto Beef; never apply Fukui's 若狭牛 label to an Ishikawa store).
- **food_culture_kb:** cultural narrative is `[CANONICAL]` **only** if the dish is in
  this KB. If it isn't, the narrative is `[INFERRED]` and must be flagged as such —
  do not generate an authoritative-sounding origin story (we have caught the model
  inventing dish histories).

## When there's no match

Do **not** fabricate a canonical entry. Treat the fact as `[INFERRED]`/`[UNKNOWN]`
(so safety-relevant ones become gap questions), and optionally append a **candidate**
to `candidates/<asset>.candidates.jsonl` for a human to verify and promote later.
Never read a candidate back as `[CANONICAL]` in the same run. See
`candidates/README.md`.
