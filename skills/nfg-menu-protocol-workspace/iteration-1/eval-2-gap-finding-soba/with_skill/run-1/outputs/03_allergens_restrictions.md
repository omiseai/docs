# 03 · Allergens & restrictions — Soba shop

Derived from Stage 02 ingredients. Each allergen traces to an ingredient and
inherits the **weakest** provenance in its chain. Where the chain contains an
`[INFERRED]` or `[UNKNOWN]` link, the allergen/restriction is **not a fact** — it
is marked `→ GAP` and routed to Stage 04, never asserted in Stage 06.

Jurisdictions: JP / US / EU / CA / AU. Status values: mandatory (man) /
recommended (rec) / none. Note: **buckwheat (そば)** and **wheat (小麦)** are both
JP-mandatory; this is a soba shop, so buckwheat is the headline allergen.

---

## Dish 1 — ざるそば (Zaru soba)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| buckwheat | soba noodles | [MENU·high] (noodles present; "soba" ⇒ buckwheat) | man | none | none | none | none |
| wheat | soba noodles (blend %) + soy sauce in つゆ | [UNKNOWN] (ratio) / [INFERRED·med] (soy sauce) → GAP | man | rec | man | man | man |
| soy | soy sauce in つゆ | [INFERRED·med] → GAP | rec | rec | man | man | man |
| fish (bonito) | dashi → katsuobushi | [INFERRED·med] → GAP | rec | none | none | none | none |
| fish (mackerel/sardine) | dashi → possible saba/niboshi | [UNKNOWN] → GAP | rec | none | none | none | none |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | no (dashi contains fish) | katsuobushi in dashi | [INFERRED·med] → GAP |
| vegan | no | dashi (fish) | [INFERRED·med] → GAP |
| pescatarian | likely yes | only animal input is fish | [INFERRED·med] → GAP |
| gluten-free | no (wheat in soy sauce + likely noodle blend) | soy sauce / noodle | [INFERRED·med] / [UNKNOWN] → GAP |
| no-pork / no-beef / halal | likely yes (no meat) but soy-sauce/mirin alcohol affects halal | — | [INFERRED·low] → GAP |

### Gaps generated here
- Noodle buckwheat/wheat ratio → wheat allergen + gluten-free status.
- つゆ contains soy sauce? → soy + wheat allergen.
- Dashi: bonito only, or mackerel/sardine too? → fish allergen scope.
- Nori garnish present? (minor; not a major allergen but confirm contents.)

---

## Dish 2 — 天ぷらそば (Tempura soba)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| buckwheat | soba noodles | [MENU·high] | man | none | none | none | none |
| wheat | noodle blend + tempura batter + soy sauce in broth | [UNKNOWN] (ratio) / [INFERRED·med] (batter, soy sauce) → GAP | man | rec | man | man | man |
| egg | tempura batter (if egg-based) | [UNKNOWN] → GAP | man | man | man | man | man |
| crustacean (shrimp) | tempura item (if shrimp) | [UNKNOWN] (item identity) → GAP | man | man | man | man | man |
| soy | soy sauce in broth | [INFERRED·med] → GAP | rec | rec | man | man | man |
| sesame | frying oil (if sesame blend) | [UNKNOWN] → GAP | rec | rec | man | man | man |
| peanut | frying oil (if peanut blend) | [UNKNOWN] → GAP | man | man | man | man | man |
| fish (bonito/mackerel) | dashi | [INFERRED·med] / [UNKNOWN] → GAP | rec | none | none | none | none |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian / vegan | no (dashi fish; likely shrimp) | dashi / tempura | [INFERRED·med] / [UNKNOWN] → GAP |
| gluten-free | no (wheat batter + soy sauce + likely noodle) | batter/sauce/noodle | [INFERRED·med] / [UNKNOWN] → GAP |
| halal | uncertain — depends on frying-oil sharing, mirin alcohol, no pork | — | [UNKNOWN] → GAP |

### Gaps generated here
- Noodle buckwheat/wheat ratio (shared with Dish 1).
- Tempura item identity (shrimp ⇒ crustacean).
- Tempura batter: egg-based or not? → egg allergen.
- Frying oil: pure vegetable vs. sesame/peanut blend → sesame + peanut allergen.
- Broth soy sauce + dashi composition (shared).

---

## Dish 3 — カレーうどん (Curry udon)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| wheat | udon noodles + curry roux flour | [CANONICAL·high] (udon ⇒ wheat) | man | rec | man | man | man |
| dairy | curry roux (milk powder, common) | [UNKNOWN] → GAP | man | man | man | man | man |
| soy | soy sauce / dashi seasoning; soy in roux | [INFERRED·med] → GAP | rec | rec | man | man | man |
| fish (bonito) | dashi base | [INFERRED·med] → GAP | rec | none | none | none | none |
| beef / pork | roux extract and/or meat topping | [UNKNOWN] → GAP (NB: beef & pork are NOT JP allergen-list items; tracked here for the no-beef/no-pork/halal restrictions, not as allergens) | — | — | — | — | — |
| chicken | possible meat topping / stock | [UNKNOWN] → GAP | — | — | — | — | — |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian / vegan | likely no (dashi fish; possible meat; possible dairy) | dashi / meat / roux | [INFERRED·med] / [UNKNOWN] → GAP |
| dairy-free | no if roux contains milk | curry roux | [UNKNOWN] → GAP |
| no-pork | depends on roux extract + topping | roux / topping | [UNKNOWN] → GAP |
| no-beef | depends on roux extract + topping | roux / topping | [UNKNOWN] → GAP |
| halal | uncertain — pork extract risk + alcohol (mirin/sauce) | roux / seasoning | [UNKNOWN] → GAP |
| gluten-free | no (udon + roux flour) | noodles / roux | [CANONICAL·high] |

### Gaps generated here
- Curry roux: does it contain dairy (milk powder)? → dairy allergen.
- Curry roux/broth: animal stock or extract (beef/pork/chicken)? → no-beef/no-pork/halal/vegetarian.
- Meat topping: pork, beef, chicken, or none? → same restrictions.

---

## Dish 4 — そばがき (Sobagaki)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| buckwheat | buckwheat flour (primary, high concentration) | [INFERRED·high] (definitional) | man | none | none | none | none |
| wheat | only if wheat flour blended in, or if dipped in soy-sauce/つゆ | [UNKNOWN] → GAP | man | rec | man | man | man |
| soy | if dipping sauce contains soy sauce | [UNKNOWN] → GAP | rec | rec | man | man | man |
| fish (bonito) | if dipped in つゆ (dashi) | [UNKNOWN] → GAP | rec | none | none | none | none |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian / vegan | depends entirely on accompaniment (sugar/kinako = yes; つゆ = no) | accompaniment | [UNKNOWN] → GAP |
| gluten-free | only if no wheat blended AND dip is wheat-free (not soy sauce/つゆ) | flour / dip | [UNKNOWN] → GAP |

### Gaps generated here
- Is any wheat flour blended into the sobagaki? → wheat allergen / gluten-free.
- What is it served/dipped with (soy sauce + wasabi / sugar + kinako / つゆ)? →
  soy + wheat + fish allergen and vegetarian/vegan status.

---

## Notes on hard-won rules applied
- No gelatin present on this menu — no meat-allergen mis-token risk here.
- Pork-free / halal handled strictly as **restrictions**, not allergens.
- Beef/pork/chicken are NOT on the JP 32-item allergen list; tracked only for the
  restriction layer (no-beef / no-pork / halal / vegetarian).
- No desserts on this menu (sobagaki is savory/plain), so the dessert-mistag class
  of error does not apply.
- Every allergen above with an `[INFERRED]`/`[UNKNOWN]` link is marked `→ GAP` and
  is carried to Stage 04, not asserted as fact.
