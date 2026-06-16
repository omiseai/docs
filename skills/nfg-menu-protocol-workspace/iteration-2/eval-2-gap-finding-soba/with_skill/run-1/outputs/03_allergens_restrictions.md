# 03 · Allergens & restrictions — Soba shop (`soba-shop-onboarding`)

Allergens DERIVED from Stage 02 ingredients (never tagged ad hoc). Each allergen
traces to an ingredient and inherits the **weakest** provenance in its chain — so any
chain touching an `[INFERRED]`/`[UNKNOWN]` ingredient yields a **GAP**, not a fact.
Jurisdiction statuses: man(datory) / rec(ommended) / none. (JP / US / EU / CA / AU.)

Note: **buckwheat (そば)** is JP-mandatory and EU-recommended; it is the central
allergen of this venue and is present (by definition) in every soba dish below.

---

## Dish 1 — ざるそば
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| buckwheat | buckwheat flour (the noodle) | [INFERRED·high] → near-certain but owner-confirm | man | none | rec | none | none |
| wheat | (a) つなぎ wheat in noodle? (二八 vs 十割) — UNKNOWN; (b) soy sauce in tsuyu | [INFERRED·med] / [UNKNOWN] → **GAP** | man | man | man | man | man |
| soy | soy sauce in tsuyu | [INFERRED·high] → **GAP** | rec | man | man | man | man |
| fish | dashi → katsuobushi (bonito) | [INFERRED·med] → **GAP** | rec | man | man | man | man |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | likely **no** | dashi (bonito = fish) in tsuyu | [INFERRED·med] → GAP (if kombu-only dashi, could be veg) |
| vegan | likely no | dashi (fish) | [INFERRED·med] → GAP |
| pescatarian | likely yes | only animal input is fish dashi | [INFERRED·med] → GAP |
| gluten-free | **no** | buckwheat is GF but wheat in noodle/tsuyu is not | [INFERRED·med] → GAP |
| no-pork / no-beef / halal | likely yes (no meat) | no meat ingredients | [INFERRED·med] (alcohol in mirin may fail strict halal) → GAP |

### Gaps generated here
- Noodle wheat ratio (二八/十割) → wheat allergen + gluten-free
- Tsuyu composition (soy sauce → soy+wheat; dashi → fish) → soy/wheat/fish + vegetarian/vegan

---

## Dish 2 — 天ぷらそば
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| buckwheat | soba noodle | [INFERRED·high] → confirm | man | none | rec | none | none |
| wheat | noodle つなぎ? + tempura batter + soy sauce | [INFERRED·high] → **GAP** | man | man | man | man | man |
| egg | tempura batter (if egg-based) | [INFERRED·med] → **GAP** | rec | man | man | man | man |
| **shrimp / crustacean** | the tempura item (if 海老天) | [UNKNOWN] → **GAP (high priority)** | man | man | man | man | man |
| sesame | frying oil (if blend contains sesame) | [UNKNOWN] → **GAP** | rec | man | man | none | none |
| soy | soy sauce in broth | [INFERRED·high] → **GAP** | rec | man | man | man | man |
| fish | dashi → katsuobushi | [INFERRED·med] → **GAP** | rec | man | man | man | man |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian / vegan | likely no | fish dashi; possible shrimp tempura | [INFERRED/UNKNOWN] → GAP |
| pescatarian | depends on tempura item | if shrimp/veg yes; — | [UNKNOWN] → GAP |
| gluten-free | **no** | wheat batter + broth + noodle | [INFERRED·high] → GAP confirm |
| no-pork / no-beef | likely yes | no meat seen | [INFERRED·med] → GAP |
| halal | likely no | alcohol (mirin), oil/cross-contam unknown | [INFERRED·low] → GAP |

### Gaps generated here
- Tempura item identity → shrimp/crustacean allergen (top safety priority)
- Batter egg content → egg allergen
- Frying oil (pure veg vs sesame blend) → sesame allergen
- Broth soy sauce + dashi → soy/wheat/fish
- Noodle wheat ratio → wheat

---

## Dish 3 — カレーうどん
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| wheat | udon (wheat by definition) + curry roux flour + soy sauce | [INFERRED·high] → **GAP** confirm | man | man | man | man | man |
| **milk** | curry roux (some contain milk powder) | [INFERRED·low] → **GAP** | rec | man | man | man | man |
| soy | soy sauce/soy seasoning in broth; possible aburaage | [INFERRED·med] → **GAP** | rec | man | man | man | man |
| fish | dashi base in curry-udon broth | [INFERRED·med] → **GAP** | rec | man | man | man | man |
| **chicken / pork / beef** | meat in curry (identity unknown) | [UNKNOWN] → **GAP** | (chicken JP rec; beef/pork JP rec) per item | man | man | varies | varies |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| **no-pork** | **UNKNOWN** | meat identity in curry unknown | [UNKNOWN] → **GAP (religious)** |
| **no-beef** | **UNKNOWN** | meat identity unknown | [UNKNOWN] → **GAP** |
| **halal** | likely no / UNKNOWN | meat source + alcohol + roux animal extract | [UNKNOWN] → **GAP** |
| vegetarian / vegan | likely no | dashi + likely meat | [INFERRED/UNKNOWN] → GAP |
| gluten-free | **no** | wheat udon + roux | [INFERRED·high] → GAP confirm |
| dairy-free | UNKNOWN | roux milk content | [INFERRED·low] → GAP |

### Gaps generated here
- Curry meat identity (none/chicken/pork/beef) → meat allergens + no-pork/no-beef/halal
- Curry roux dairy content → milk allergen + dairy-free
- Roux/broth wheat + soy + dashi → wheat/soy/fish

---

## Dish 4 — そばがき
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| buckwheat | buckwheat flour | [INFERRED·high] → confirm | man | none | rec | none | none |
| wheat | only if つなぎ wheat added (usually none) OR accompanying tsuyu soy sauce | [INFERRED·med] / [UNKNOWN] → **GAP** | man | man | man | man | man |
| soy | accompanying tsuyu soy sauce (if served with dip) | [INFERRED·med] → **GAP** | rec | man | man | man | man |
| fish | accompanying tsuyu dashi | [INFERRED·med] → **GAP** | rec | man | man | man | man |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian / vegan | depends on accompaniment (plain sobagaki is veg/vegan; tsuyu adds fish) | [INFERRED·med] → GAP |
| gluten-free | possibly **yes** if no wheat tsunagi and no soy-sauce dip | [UNKNOWN] → **GAP** |
| no-pork / no-beef / halal | likely yes | no meat | [INFERRED·med] → GAP |

### Gaps generated here
- Whether sobagaki contains any wheat tsunagi → wheat / gluten-free (it may be the
  one wheat-free dish — worth confirming as a safe recommendation)
- What it is served with (plain / soy dip / dashi tsuyu) → soy/fish + vegetarian

---

## Cross-cutting safety note
Buckwheat is a **severe, anaphylaxis-class** allergen. EVERY dish in this shop (and
likely the whole kitchen) involves buckwheat. Even the curry udon (wheat noodle) is
made in a kitchen handling buckwheat flour → **cross-contamination** is a real risk
for buckwheat-allergic diners. This is itself a gap question for the operator (shared
equipment / shared boiling water).
