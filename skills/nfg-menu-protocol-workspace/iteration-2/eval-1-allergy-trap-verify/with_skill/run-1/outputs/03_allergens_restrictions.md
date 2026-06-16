# 03 · Allergens & restrictions — (Unnamed store — lunch menu)

Derived **mechanically from Stage 02 ingredients only**. Each allergen traces to a
named ingredient and inherits the **weakest** provenance in its chain. Because the
source printed only names + prices, essentially every chain runs through an
`[INFERRED]` or `[UNKNOWN]` ingredient → so essentially every allergen status is a
**GAP**, not a fact. None may be written as fact into Stage 06.

Status legend: `rec` = recommended labeling, `man` = mandatory labeling, `none` = not
in that jurisdiction's list, `—` = not yet determinable (chain unresolved).

---

## Dish 1 — ロースかつ定食 (Pork loin cutlet set meal)
### Allergens (JP / US / EU / CA / AU)
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| wheat | breading flour + panko + (sauce soy sauce) | [INFERRED·med] → **GAP** | man | man | man | man | man |
| egg | breading batter | [INFERRED·med] → **GAP** | man | man | man | none | man |
| soy | miso soup (miso/tofu) + tonkatsu sauce (soy sauce) | [INFERRED·med] → **GAP** | rec | man | man | man | man |
| fish | miso-soup dashi → katsuobushi (bonito) | [INFERRED·med] → **GAP** | rec | man | man | man | man |
| sesame | frying-oil base (if blended with sesame oil) | [UNKNOWN] → **GAP** | rec | man | man | man | man |
| peanut | frying-oil base (if peanut oil) | [UNKNOWN] → **GAP** | rec | man | man | man | man |

Pork itself: pork is **not** an allergen token — it is a restriction matter (see below).

### Restrictions (12-item master)
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | no (contains pork; dashi likely fish) | pork loin | [INFERRED·high] → GAP (confirm pork) |
| vegan | no | pork + dairy(sauce?)/fish | [INFERRED·high] |
| no-pork | **fails** (contains pork) | pork loin | [INFERRED·high] → GAP (confirm pork) |
| halal | **fails** (pork; frying-oil & sauce unconfirmed) | pork loin | [INFERRED·high] → GAP |
| no-beef | likely ok (no beef expected) | — | [INFERRED·low] |
| gluten-free | **fails** (breading wheat) | breading | [INFERRED·med] → GAP |

### Gaps generated here
- Breading make-up (wheat? egg? potato starch?) → wheat + egg status
- Frying-oil base → sesame / peanut status
- Miso soup presence & make-up (it is an *inferred* accompaniment) → soy + fish status
- Tonkatsu sauce presence & make-up → soy + wheat status
- Confirm the protein is pork → no-pork / halal / vegetarian

---

## Dish 2 — エビフライ (Fried shrimp / ebi-fry)
### Allergens (JP / US / EU / CA / AU)
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| shrimp / crustacean | shrimp (the dish itself) | [INFERRED·high] → **GAP** (confirm) | man | man | man | man | man |
| wheat | breading flour + panko | [INFERRED·med] → **GAP** | man | man | man | man | man |
| egg | breading batter + (tartar sauce mayo?) | [INFERRED·med] → **GAP** | man | man | none | none | man |
| sesame | frying-oil base (if blended) | [UNKNOWN] → **GAP** | rec | man | man | man | man |
| peanut | frying-oil base (if peanut oil) | [UNKNOWN] → **GAP** | rec | man | man | man | man |

Note: shrimp/crustacean is the headline allergen and is near-certain from the name,
but per the iron rule the chain still runs through `[INFERRED]` (the source never
prints "shrimp" as an ingredient list), so even this is flagged for operator
confirmation rather than asserted as fact. The **hidden** allergens (wheat, egg,
oil) are the real traps.

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| pescatarian | ok (seafood, no land meat expected) | shrimp | [INFERRED·med] |
| vegetarian / vegan | no (shellfish) | shrimp | [INFERRED·high] |
| gluten-free | **fails** (breading wheat) | breading | [INFERRED·med] → GAP |
| halal | unconfirmed (oil/sauce) | frying oil | [UNKNOWN] → GAP |

### Gaps generated here
- Confirm crustacean (shrimp) and whether any other shellfish/cross-contact
- Breading make-up → wheat + egg
- Frying-oil base → sesame / peanut
- Accompanying sauce (tartar = egg) → egg

---

## Dish 3 — 杏仁豆腐 (Annin-dofu / almond jelly)
**Naming-trap guard:** "豆腐" in the name is a texture word. Do **NOT** derive a soy
allergen from the name. Soy is only derivable if an actual soy ingredient is present
(none expected). **Dessert-mistagging guard:** do not assign meat/pork/beef allergens
to this dessert; any gelatin question is a *restriction* matter from the setting
agent, never a meat allergen.

### Allergens (JP / US / EU / CA / AU)
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| milk (dairy) | milk/cream base | [INFERRED·med] → **GAP** | rec | man | man | man | man |
| almond (tree nut) | almond flavor *if* real almond/apricot-kernel | [UNKNOWN] → **GAP** | rec(JP: not in core list) | man | man | man | man |
| soy | — (NONE; name "豆腐" is not soy) | n/a | none | none | none | none | none |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | depends on setting agent (agar=ok / gelatin=fails) | setting agent | [UNKNOWN] → GAP |
| vegan | no (dairy) + setting agent | milk | [INFERRED·med] → GAP |
| halal / kosher | depends on gelatin source (porcine/bovine?) | setting agent | [UNKNOWN] → GAP |
| dairy-free | likely **fails** (milk) | milk | [INFERRED·med] → GAP |

### Gaps generated here
- Dairy presence (milk/cream)? → milk allergen
- Almond flavor = real apricot-kernel/almond vs synthetic essence? → tree-nut allergen
- Setting agent = agar vs gelatin (and if gelatin, source)? → vegetarian/halal/kosher

---

## Dish 4 — コーヒーゼリー (Coffee jelly)
**Dessert-mistagging guard** as above. Gelatin (if present) is its own token and is
**not** a meat allergen.

### Allergens (JP / US / EU / CA / AU)
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| milk (dairy) | cream/milk topping (if served) | [UNKNOWN] → **GAP** | rec | man | man | man | man |

(No other allergen derivable from coffee + sugar + setting agent. Coffee itself is
not on the 32-item list.)

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | depends on setting agent (agar=ok / gelatin=fails) | setting agent | [UNKNOWN] → GAP |
| vegan | depends on setting agent + dairy topping | setting agent + topping | [UNKNOWN] → GAP |
| halal / kosher | depends on gelatin source | setting agent | [UNKNOWN] → GAP |
| dairy-free | depends on topping | topping | [UNKNOWN] → GAP |

### Gaps generated here
- Setting agent = agar vs gelatin (and if gelatin, source)? → vegetarian/halal/kosher
- Topping = cream/milk vs none? → milk allergen / dairy-free
