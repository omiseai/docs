# 01 · Source capture — Lunch Menu (store name not provided)

- Run date: 2026-06-16
- data_source: live
- Operator availability: NOT available this run (operator-dialogue stage deferred — see Stage 05)
- Canonical asset files (product_master.json, ingredient_glossary.json, food-culture KB)
  not present on disk for this run → canonical matching done from documented asset
  knowledge only, and any uncertain match is left as [INFERRED], not asserted as [CANONICAL].
- Sources received:
  - Pasted plain text (4 line items between `--- LUNCH MENU ---` and `--- END ---`). Clean, fully legible.

## Items (verbatim, original language)

### (no section header printed — single "LUNCH MENU" block)
| # | Printed name | Printed description | Price | Notes on legibility |
|---|---|---|---|---|
| 1 | ロースかつ定食 | — | ¥1000 | clear |
| 2 | エビフライ | — | ¥1200 | clear |
| 3 | 杏仁豆腐 | — | ¥350 | clear |
| 4 | コーヒーゼリー | — | ¥300 | clear |

(Transcribe only. No interpretation, no translation here.)

## Notes on what the source does NOT tell us
- No ingredient lists, no preparation notes, no allergen labels printed.
- No frying-oil disclosure, no breading composition, no garnish/topping disclosure.
- "定食" (set meal) for item 1 implies accompanying items (rice, miso soup, pickles,
  shredded cabbage) by Japanese convention, but NONE of those are printed — so they
  are assumptions, handled as gaps downstream, not recorded as fact here.
