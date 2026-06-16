# 03 · Allergens & restrictions — Torihei (鳥平), Osaka izakaya

Derived from Stage 02 ingredients only — never tagged ad hoc. Each allergen traces
to a specific ingredient and inherits the **weakest provenance** in its chain. Any
allergen/restriction resting on `[INFERRED]` or `[UNKNOWN]` is **not asserted** — it
becomes a gap (Stage 04).

Allergen status codes: man = mandatory label, rec = recommended, none = not listed.
Jurisdictions: JP / US / EU / CA / AU.

Reminders honored: gelatin is its own token (not a meat allergen); pork-free/halal
is a **restriction**, not an allergen; an allergen must trace to a real ingredient
(no dessert-style mass-mistagging).

---

## Dish 1 — 牛すじ煮込み (Beef tendon stew)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| fish (bonito) | dashi → katsuobushi | [INFERRED·med] → GAP | rec | none | none | none | none |
| soy | seasoning base (miso/soy sauce) | [UNKNOWN] → GAP | rec | man | man | man | man |
| wheat | IF soy-sauce base | [UNKNOWN] → GAP | man | man | man | man | man |

(No allergen asserted as fact — all three rest on inferred/unknown chains.)

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | no (beef) | beef tendon | [MENU·high] |
| vegan | no | beef tendon | [MENU·high] |
| no-beef | fails | beef tendon | [MENU·high] |
| halal | no (beef not halal-slaughtered unless stated; alcohol/mirin possible) | beef tendon + seasoning | [INFERRED·med] → GAP |

### Gaps generated here
- Seasoning base (miso vs soy sauce vs mirin) → soy + wheat allergen, halal status.
- Dashi composition → fish allergen.

---

## Dish 2 — 鶏の唐揚げ (Japanese fried chicken / karaage)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| soy | marinade soy sauce | [INFERRED·med] → GAP | rec | man | man | man | man |
| wheat | soy sauce AND/OR flour coating | [UNKNOWN] (coating) → GAP | man | man | man | man | man |
| sesame | frying oil (if sesame blend) | [UNKNOWN] → GAP | rec | man | man | man | man |

(Coating could be pure potato starch = no wheat; cannot assert either way → gap.)

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | no (chicken) | chicken | [MENU·high] |
| vegan | no | chicken | [MENU·high] |
| no-pork | likely ok | chicken (no pork in standard karaage) | [INFERRED·med] |
| halal | no (frying oil/marinade alcohol; chicken not halal-slaughtered unless stated) | marinade + prep | [INFERRED·med] → GAP |
| gluten-free | undetermined | coating + soy | [UNKNOWN] → GAP |

### Gaps generated here
- Coating composition (potato starch vs wheat flour) → wheat / gluten-free.
- Frying oil type (sesame blend?) → sesame.
- Marinade soy presence → soy.

---

## Dish 3 — だし巻き卵 (Rolled dashi omelette)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| egg | egg | [MENU·high] ✅ ASSERTED | man | man | man | man | man |
| fish (bonito) | dashi → katsuobushi | [INFERRED·med] → GAP | rec | none | none | none | none |
| soy | seasoning soy sauce | [INFERRED·med] → GAP | rec | man | man | man | man |
| wheat | IF soy sauce used | [INFERRED·low] → GAP | man | man | man | man | man |

(Egg is the one **asserted** allergen in this run — it rests on [MENU·high].)

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | yes (if dashi is the only animal product, still contains fish → NOT vegetarian) | dashi fish | [INFERRED·med] → GAP |
| vegan | no (egg) | egg | [MENU·high] |
| pescatarian | possibly yes | egg + fish dashi | [INFERRED·med] |
| dairy-free | yes (no dairy) | — | [INFERRED·high] |

### Gaps generated here
- Dashi fish content → fish allergen + vegetarian status.
- Seasoning soy sauce → soy + wheat.

---

## Dish 4 — ポテトサラダ (Potato salad)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| egg | mayonnaise → egg yolk | [INFERRED·high] → GAP | man | man | man | man | man |
| (mustard) | IF mayo/seasoning contains mustard | [UNKNOWN] → GAP | none | none | man (EU) | none | none |

(Egg is the typical mayonnaise binder but the binder itself is inferred — so even
egg here is NOT asserted; it is a gap. Mayonnaise composite expanded per rule.)

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | undetermined | possible ham/bacon | [INFERRED·low] → GAP |
| vegan | no (mayo egg) | mayonnaise | [INFERRED·high] → GAP |
| no-pork | undetermined | possible ham/bacon | [UNKNOWN] → GAP |
| halal | undetermined | possible pork | [UNKNOWN] → GAP |

### Gaps generated here
- Binder identity (mayonnaise → egg) → egg allergen.
- Presence/type of cured meat (ham/bacon = pork?) → no-pork, halal, vegetarian.
- Mustard in dressing → EU mustard allergen.

---

## Dish 5 — 本日の刺身盛り合わせ (Today's assorted sashimi)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| fish (species TBD) | raw fish assortment | [UNKNOWN] → GAP | varies | man | man | man | man |
| crustacean/shrimp | possible 海老 garnish or item | [UNKNOWN] → GAP | rec | man | man | man | man |
| salmon roe (いくら) | possible component | [UNKNOWN] → GAP | rec (JP) | none | none | none | none |
| abalone (あわび) | possible component | [UNKNOWN] → GAP | rec (JP) | none | none | none | none |
| soy + wheat | dipping soy sauce | [INFERRED·med] → GAP | rec/man | man | man | man | man |

(Nothing asserted. The fish are not knowable from a static record — daily-rotating.)

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | no (raw fish) | fish | [MENU·high] |
| vegan | no | fish | [MENU·high] |
| pescatarian | yes | fish only | [INFERRED·med] |
| no-pork / halal | fish ok but raw shellfish not kosher; alcohol n/a | — | [INFERRED·low] |

### Gaps generated here
- **Daily fish species list** → entire allergen profile (fish / crustacean / roe / abalone / squid / etc.). This is a recurring, per-service gap, not a one-time fix.
- Dipping soy sauce → soy + wheat.

---

## Dish 6 — 黒龍 純米吟醸 (Kokuryū Junmai Ginjō, glass)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| (none from rice/water/koji/yeast) | canonical spec | [CANONICAL·high] ✅ | none | none | none | none | none |
| sulphites | added-sulphite check | [INFERRED·low] → minor GAP | none | none | rec | none | none |

(Sake is generally not added-sulphite; flagged low, not asserted. No food allergens
derive from junmai ginjō ingredients per product_master.)

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| no-alcohol | fails (alcoholic beverage) | sake | [CANONICAL·high] ✅ ASSERTED |
| vegan / vegetarian | yes (no animal products in junmai) | canonical spec | [CANONICAL·high] |
| halal | fails (alcohol) | sake | [CANONICAL·high] ✅ ASSERTED |
| gluten-free | yes (rice-based, no wheat) | canonical spec | [CANONICAL·high] |

### Gaps generated here
- Added sulphites (low priority, EU-relevant only).

---

## Summary of asserted-as-fact allergens/restrictions (rest on [MENU]/[CANONICAL])
- Dish 3: **egg = yes** [MENU·high].
- Dish 6: **no-alcohol = fails, halal = fails, vegan/vegetarian = yes, gluten-free = yes** [CANONICAL·high].
- All beef/chicken/fish "vegetarian = no" statuses [MENU·high] (dish names state the protein).
- Everything else is a GAP — see Stage 04.
