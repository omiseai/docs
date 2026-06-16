# 03 · Allergens & restrictions — Torihei

Derived from Stage 02 ingredients. Each allergen traces to a specific ingredient and
inherits the **weakest** provenance in its chain. Status across JP / US / EU / CA / AU
(mandatory `mand` / recommended `rec` / none). Any allergen whose chain rests on
`[INFERRED]` or `[UNKNOWN]` is **not asserted as fact** — it is flagged → GAP.

---

## Dish 1 — 牛すじ煮込み (Beef tendon stew)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| fish (bonito) | dashi → katsuobushi | [INFERRED·med] → GAP | rec | none | none | none | none |
| soy | seasoning base (miso/soy sauce) | [UNKNOWN] → GAP | rec | mand | mand | mand | mand |
| wheat | IF soy-sauce base | [UNKNOWN] → GAP | mand | mand | mand | mand | mand |
### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian / vegan | no (contains beef) | beef tendon | [MENU·high] |
| pescatarian | no (contains beef) | beef tendon | [MENU·high] |
| no-beef | no (contains beef) | beef tendon | [MENU·high] |
| hindu | no (beef) | beef tendon | [MENU·high] |
| halal | likely no (alcohol/mirin in dashi-stew common; beef would need halal slaughter) | seasoning/meat | [INFERRED·low] → GAP |
### Gaps generated here
- Seasoning base (miso vs soy sauce) → soy, and wheat if soy sauce
- Dashi composition → fish (bonito)

## Dish 2 — 鶏の唐揚げ (Chicken karaage)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| wheat | coating (flour?) AND/OR marinade soy sauce | [UNKNOWN] → GAP | mand | mand | mand | mand | mand |
| soy | marinade soy sauce | [INFERRED·med] → GAP | rec | mand | mand | mand | mand |
| sesame | frying oil (if sesame blend) | [UNKNOWN] → GAP | rec | mand | mand | mand | mand |
### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian / vegan | no (chicken) | chicken | [MENU·high] |
| no-beef / no-pork | yes-ok (chicken only, IF no shared-fryer pork) | chicken | [INFERRED·med] → GAP (cross-contact) |
| halal | likely no (non-halal chicken + soy/alcohol marinade) | chicken/marinade | [INFERRED·low] → GAP |
| gluten-free | unknown (coating may be potato starch → GF, or wheat → not) | coating | [UNKNOWN] → GAP |
### Gaps generated here
- Coating: potato starch vs wheat flour → wheat / gluten-free
- Frying oil: sesame blend? → sesame
- Marinade contains soy sauce? → soy, wheat

## Dish 3 — だし巻き卵 (Dashimaki tamago)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| egg | egg | [MENU·high] | mand | mand | mand | mand | mand |
| fish (bonito) | dashi → katsuobushi | [INFERRED·med] → GAP | rec | none | none | none | none |
| soy | seasoning soy sauce (if used) | [INFERRED·low] → GAP | rec | mand | mand | mand | mand |
| wheat | IF soy sauce in seasoning | [INFERRED·low] → GAP | mand | mand | mand | mand | mand |
### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | yes-ok IF dashi is kombu-only; no if katsuo dashi | egg + dashi | [INFERRED·med] → GAP |
| vegan | no (egg) | egg | [MENU·high] |
| pescatarian | yes-ok | egg/dashi | [MENU·high] |
### Gaps generated here
- Dashi composition (katsuo vs kombu-only) → fish allergen + vegetarian status
- Seasoning soy sauce? → soy, wheat

## Dish 4 — ポテトサラダ (Potato salad)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| egg | mayonnaise → egg yolk | [INFERRED·high] → GAP | mand | mand | mand | mand | mand |
| (pork) — see restriction, not allergen | ham/bacon if present | [INFERRED·low] → GAP | — | — | — | — | — |
### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegan | no (mayo egg) | mayonnaise | [INFERRED·high] → GAP |
| vegetarian | yes-ok IF no ham/bacon | ham/bacon? | [INFERRED·low] → GAP |
| no-pork / halal | unknown (ham/bacon?) | ham/bacon? | [INFERRED·low] → GAP |
### Gaps generated here
- Mayonnaise present (egg)? → egg (very likely but unconfirmed)
- Ham/bacon present? → pork / no-pork / halal / vegetarian
- Note: pork is filed under **restriction**, not allergen (per allergen rules).

## Dish 5 — 本日の刺身盛り合わせ (Today's assorted sashimi)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| fish | raw fish (kind certain, species unknown) | [INFERRED·high] → GAP (which species) | rec | mand | mand | mand | mand |
| salmon roe (ikura) | possible component | [UNKNOWN] → GAP | rec | none | none | none | none |
| crab | possible component | [UNKNOWN] → GAP | mand | mand | mand | mand | mand |
| shrimp/prawn | possible component | [UNKNOWN] → GAP | mand | mand | mand | mand | mand |
| squid/abalone | possible component | [UNKNOWN] → GAP | rec | mand | mand | mand | mand |
| soy + wheat | accompanying soy sauce | [INFERRED·med] → GAP | rec/mand | mand | mand | mand | mand |
### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegan / vegetarian | no (raw fish) | fish | [INFERRED·high] |
| pescatarian | yes-ok | fish | [INFERRED·high] |
| no-beef / no-pork | yes-ok | fish only | [INFERRED·high] |
| halal | no (soy sauce + non-halal fish handling typical; also shellfish concerns) | fish/accompaniment | [INFERRED·low] → GAP |
### Gaps generated here
- Daily species list → which fish; shellfish/cephalopod/roe present? (multiple allergens)
- This dish is inherently daily-variable — species-level allergy answers require a
  daily operator input, not a one-time confirmation.

## Dish 6 — 黒龍 純米吟醸 (Kokuryu Junmai Ginjo)
### Allergens
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| (none) | rice, koji, water | [CANONICAL·high] | none | none | none | none | none |
### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| no-alcohol | FAIL (contains alcohol, ~15.5% ABV) | sake | [CANONICAL·high] |
| halal | no (alcohol) | sake | [CANONICAL·high] |
| vegan / vegetarian | yes-ok (junmai: rice/koji/water; no animal products) | sake | [CANONICAL·high] |
| gluten-free | yes-ok (rice-based, no wheat) | sake | [CANONICAL·high] |
### Gaps generated here
- None. Fully verified via product_master.

---

## Cross-cutting safety note
The two dashi-bearing dishes (1, 3) share the same katsuobushi → fish question; the
soy-sauce question recurs across dishes 1, 2, 3, 5. These are per-dish gaps even
though the likely answer is shared — a "we use the same X everywhere" operator answer
would resolve them, but until then each stays OPEN per dish (no cascading of guesses).
