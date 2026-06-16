# 03 · Allergens & restrictions — Lunch Menu

Derived from Stage 02 ingredients. Each allergen traces to an ingredient and inherits
the **weakest** provenance in its chain. Any allergen whose chain rests on
[INFERRED]/[UNKNOWN] is NOT a fact — it becomes a gap (Stage 04), never asserted in
Stage 06. Status codes per jurisdiction: man = mandatory label, rec = recommended, none.

Allergen-label note: shrimp/prawn (crustacean) and wheat and egg are JP-mandatory (特定原材料);
soybean and milk are JP-recommended (特定原材料に準ずるもの). US/EU/CA/AU treat crustacean,
egg, milk, wheat, soy as major allergens (man), with jurisdictional nuance.

---

## Dish 1 — ロースかつ定食 (Pork loin cutlet set)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| wheat | breading: flour + panko | [INFERRED·high] → GAP | man | man | man | man | man |
| egg | breading: egg wash | [INFERRED·high] → GAP | man | man | man | man | man |
| soy | tonkatsu sauce → soy sauce | [INFERRED·med] → GAP | rec | man | man | man | man |
| (wheat via soy sauce) | tonkatsu sauce → soy sauce | [INFERRED·med] → GAP | man | man | man | man | man |
| sesame / peanut | frying oil (type unknown) | [UNKNOWN] → GAP | (sesame: man JP) | man | man | man | man |
| soy / milk / fish | miso-soup & sides (if part of 定食) | [UNKNOWN] → GAP | rec | man | man | man | man |

- No allergen here is asserted as fact; ALL are gaps (breading + sauce + oil + sides all undisclosed).

### Restrictions (12-item master)
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian / vegan | no (meat) | pork loin (animal) | [INFERRED·high] (species inferred; that it is meat is high) |
| no-pork / halal / kosher | no IF pork | meat species | [INFERRED·high] → GAP (species not printed; if chicken-loin, no-pork could flip) |
| no-beef | likely yes (no beef) | — | [INFERRED·med] |
| gluten-free | no | breading wheat | [INFERRED·high] |
| pescatarian | no | meat | [INFERRED·high] |
| dairy-free | undetermined | sauce/sides | [UNKNOWN] → GAP |

### Gaps generated here
- Breading composition (wheat/egg) — inferred, must confirm → wheat, egg
- Tonkatsu sauce presence/recipe → soy, wheat
- Frying oil type → sesame / peanut
- Meat species (pork vs chicken/beef) → halal/no-pork/kosher restriction
- Set-meal sides (esp. miso soup) → soy, fish, milk

---

## Dish 2 — エビフライ (Fried prawn)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| **crustacean (shrimp/prawn)** | shrimp | **[MENU·high] → FACT** | man | man | man | man | man |
| wheat | breading: flour + panko | [INFERRED·high] → GAP | man | man | man | man | man |
| egg | breading: egg wash | [INFERRED·high] → GAP | man | man | man | man | man |
| sesame / peanut | frying oil (type unknown) | [UNKNOWN] → GAP | (sesame man JP) | man | man | man | man |
| egg / milk | tartar sauce (if served) | [UNKNOWN] → GAP | man | man | man | man | man |

- **Crustacean is the single asserted-as-FACT allergen on this menu** — it traces directly
  to the printed dish name (エビ = shrimp), [MENU·high]. Everything else is a gap.

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian / vegan / pescatarian-meat | no | shrimp (crustacean) | [MENU·high] |
| pescatarian | yes (seafood OK) | shrimp | [MENU·high] |
| halal/kosher | kosher = no (shellfish) | shrimp | [MENU·high]; halal undetermined (oil/sauce) → GAP |
| gluten-free | no | breading wheat | [INFERRED·high] |
| dairy-free | undetermined | tartar sauce | [UNKNOWN] → GAP |

### Gaps generated here
- Breading composition (wheat/egg) — confirm
- Frying oil type → sesame / peanut
- Accompanying sauce (tartar → egg/dairy) presence/recipe

---

## Dish 3 — 杏仁豆腐 (Annin dofu)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| milk | dairy (common recipe) | [INFERRED·med] → GAP | rec | man | man | man | man |
| tree-nut (almond) | almond essence / actual almond | [UNKNOWN] → GAP | (almond: man JP since 2025) | man | man | man | man |

- **TRAP — soy NOT derived:** the name 豆腐 ("tofu") does NOT introduce soybean. No
  soybean ingredient is present in the decomposition → no soy allergen. (Confirm no
  soy-based gelling/thickener with operator anyway — listed as gap.)
- **DESSERT guard:** no beef/pork attached. If a gelling agent turns out to be gelatin,
  gelatin is its OWN token, NOT a meat allergen — and gelatin is not on the major-allergen
  lists; it only matters for the vegan restriction.

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | undetermined | gelling agent (gelatin vs agar) | [UNKNOWN] → GAP |
| vegan | likely no | dairy + possible gelatin | [INFERRED·med] → GAP |
| dairy-free | undetermined | milk | [INFERRED·med] → GAP |
| halal / kosher | undetermined | gelatin source (if gelatin, animal origin matters) | [UNKNOWN] → GAP |
| no-pork/no-beef | undetermined | gelatin source | [UNKNOWN] → GAP |

### Gaps generated here
- Gelling agent: agar vs gelatin (and if gelatin, animal source) → vegan, halal, no-pork/beef
- Dairy presence (milk vs water/coconut base) → milk allergen
- Almond/apricot-kernel: real tree-nut almond used? → tree-nut allergen
- Confirm NO soy ingredient despite the "tofu" name

---

## Dish 4 — コーヒーゼリー (Coffee jelly)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| milk | cream / creamer topping (if served) | [UNKNOWN] → GAP | rec | man | man | man | man |

- **DESSERT guard + gelatin rule:** if gelled with gelatin, gelatin is its own token and
  is NOT a meat allergen → no beef/pork allergen derived. Gelatin only affects vegan +
  (if animal-source) halal/kosher restrictions.

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | undetermined | gelling agent (gelatin vs agar) | [UNKNOWN] → GAP |
| vegan | undetermined | gelatin + cream | [UNKNOWN] → GAP |
| dairy-free | undetermined | cream topping | [UNKNOWN] → GAP |
| halal / kosher | undetermined | gelatin source | [UNKNOWN] → GAP |
| no-alcohol | likely yes | (coffee, no alcohol) | [INFERRED·med] |

### Gaps generated here
- Gelling agent: gelatin vs agar (and if gelatin, animal source) → vegan, halal, no-pork/beef
- Cream / creamer / milk topping presence → milk allergen
- Garnish (condensed milk, syrup) → milk

---

## Cross-dish summary of derivation integrity
- Only ONE allergen on the whole menu is asserted as fact: **crustacean (Dish 2)**, from [MENU].
- Every other allergen rests on [INFERRED]/[UNKNOWN] and is therefore a GAP, not a fact.
- No dessert was tagged with beef/pork. Gelatin (if present) kept as its own token, not a meat allergen.
- Soy was NOT auto-derived for 杏仁豆腐 from the "tofu" name.
