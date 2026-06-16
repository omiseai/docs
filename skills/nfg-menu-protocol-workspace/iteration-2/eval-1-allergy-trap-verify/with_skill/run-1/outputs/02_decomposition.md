# 02 · Decomposition — (Unnamed store — lunch menu)

For each dish: components → ingredients (composites expanded), cooking methods,
every field provenance-tagged. Canonical assets checked per dish; **no dish or
ingredient matched a seed canonical entry** (see notes), so nothing here is tagged
`[CANONICAL]`. The source printed only names + prices, so almost everything below is
`[INFERRED]` from culinary norms and must be verified.

Canonical lookup result (recorded once):
- `product_master.json` — no beverages on this menu → no match.
- `ingredient_glossary.json` — none of these dish names / the inferred ingredients
  are seed glossary terms (タイ, カニ面, バイ貝, へしこ, 片栗粉, 能登牛, 若狭牛). No
  `[CANONICAL]` name applied. (If breading turns out to use 片栗粉/potato starch, the
  glossary entry would apply — but that is an open gap, not established.)
- `food_culture_kb.json` — none of these dishes are in the KB (only へしこ, 柿の葉寿司).
  So any cultural narrative is `[INFERRED]`, never `[CANONICAL]`.

---

## Dish 1 — ロースかつ定食 (Pork loin cutlet set meal [INFERRED·high])
- English name: Pork loin cutlet (tonkatsu) set meal  [INFERRED·high]
  (no glossary entry; standard culinary reading of ロースかつ定食)
- Components & ingredients:
  - **Cutlet itself:**
    - pork loin (ロース)  [INFERRED·high]  ← name strongly implies pork loin, but
      the source never prints "pork"; confirm it is pork (not e.g. chicken/another cut)
    - breading / batter (composite → wheat flour + egg + panko breadcrumbs[→wheat])  [INFERRED·med]
      ← "かつ" = breaded cutlet by convention; exact breading make-up unconfirmed
      (could use 片栗粉/potato starch instead of/with wheat — see glossary; this is a gap)
    - frying oil (composite → unknown base: vegetable? blend with sesame?)  [UNKNOWN]
      ← oil identity not given; determines sesame/soy/peanut oil questions
  - **Set-meal accompaniments (定食 convention — NOT printed on source):**
    - cooked rice  [INFERRED·med]
    - miso soup (composite → miso[→soy], dashi[→ kombu + katsuobushi/fish], tofu[→soy]?, wakame?)  [INFERRED·med]
    - shredded cabbage  [INFERRED·med]
    - tonkatsu sauce (composite → vegetables/fruit + sugar + vinegar + soy sauce[→soy + wheat] + spices)  [INFERRED·med]
    - pickles (tsukemono)  [UNKNOWN]
- Cooking methods (from 20-method master): deep-fry  [INFERRED·high]; boil/simmer (rice, miso soup)  [INFERRED·med]
- Notes: This is a classic allergen-trap dish — wheat + egg + soy hide in the
  breading, oil, sauce and miso soup. None of those are printed; all become gaps.

---

## Dish 2 — エビフライ (Fried shrimp / ebi-fry [INFERRED·high])
- English name: Breaded fried shrimp (ebi-fry)  [INFERRED·high]  (no glossary entry)
- Components & ingredients:
  - shrimp / prawn (エビ)  [INFERRED·high]  ← name = shrimp; printed name does not
    specify species, but the crustacean identity itself is high-confidence from the name
  - breading / batter (composite → wheat flour + egg + panko breadcrumbs[→wheat])  [INFERRED·med]
  - frying oil (composite → unknown base: vegetable? blend with sesame?)  [UNKNOWN]
  - serving sauce / tartar sauce? (composite → mayo[→egg] + …)  [UNKNOWN]  ← often
    served with tartar sauce or tonkatsu sauce; not printed
- Cooking methods: deep-fry  [INFERRED·high]
- Notes: shrimp = crustacean allergen is essentially certain from the name; the
  *added* allergens (wheat, egg, oil) are the hidden traps and remain gaps.

---

## Dish 3 — 杏仁豆腐 (Annin-dofu / almond jelly [INFERRED·high])
- English name: Annin-dofu (almond-flavored jelly)  [INFERRED·high]
  (no glossary entry; Romaji + gloss is appropriate — Japan/China-context dessert.
  **NOT** "almond tofu" / **NOT** bean-curd tofu — the "豆腐" here is a texture word,
  not soybean curd. This is a naming trap.)
- Components & ingredients (typical recipe — NOT printed):
  - milk and/or cream (dairy)  [INFERRED·med]  ← most recipes are milk-based → dairy gap
  - sugar  [INFERRED·med]
  - setting agent: agar (kanten) **or** gelatin  [UNKNOWN]
    ← which one is unknown; gelatin matters for vegetarian/halal/kosher restrictions
  - almond flavor: apricot-kernel (杏仁) extract **or** almond essence  [UNKNOWN]
    ← true 杏仁 is apricot kernel; many shops use almond essence. Affects tree-nut
      (almond) allergen status. Unknown which.
- Cooking methods: (none / chilled-set)  [INFERRED·med]
- Notes:
  - "豆腐" in the name does **NOT** mean it contains soy/tofu. Do not derive a soy
    allergen from the name. (Naming trap.)
  - This is a dessert — guard against the dessert-mistagged-with-meat error. Any
    meat/gelatin question is a *restriction* matter, derived only from an actual
    ingredient (the setting agent), never asserted.

---

## Dish 4 — コーヒーゼリー (Coffee jelly [INFERRED·high])
- English name: Coffee jelly  [INFERRED·high]  (plain English name exists → use it; no romanization)
- Components & ingredients (typical recipe — NOT printed):
  - brewed coffee  [INFERRED·high]
  - sugar  [INFERRED·med]
  - setting agent: gelatin **or** agar (kanten)  [UNKNOWN]
    ← affects vegetarian/vegan/halal/kosher restrictions
  - topping: cream / milk / condensed milk / syrup (dairy?)  [UNKNOWN]
    ← coffee jelly is commonly served with cream or milk → possible dairy; not printed
- Cooking methods: (none / chilled-set)  [INFERRED·med]
- Notes: dessert — same dessert-mistagging guard as Dish 3. Gelatin (if used) is its
  own token and is **not** a meat allergen; it is a restriction-layer matter.
