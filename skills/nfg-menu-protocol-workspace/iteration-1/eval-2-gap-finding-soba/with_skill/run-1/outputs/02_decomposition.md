# 02 · Decomposition — Soba shop

For each dish: components → ingredients (expand composites), cooking methods,
every field provenance-tagged. Operator is unavailable this run, so nothing
carries `[OPERATOR]` provenance yet — composite/seasoning/oil details are
`[INFERRED]` or `[UNKNOWN]` and flow to the gap register.

Key cross-cutting unknowns for a soba shop (drive most safety gaps):
- **Soba noodle flour ratio.** Japanese "soba" ranges from 十割 (100% buckwheat,
  wheat-free) to ニ八 (80% buckwheat / 20% wheat) to mostly-wheat blends. Buckwheat
  (そば) AND wheat (小麦) are both JP-mandatory allergens. The wheat content cannot
  be inferred — it must be confirmed per this shop's noodle.
- **Dashi / tsuyu base.** Soba dipping sauce and broth (めんつゆ) almost always
  contains soy sauce (soy + wheat) and katsuobushi (bonito/fish); some use kombu,
  some add mackerel/sardine (saba/niboshi). Exact composition is operator-specific.

---

## Dish 1 — ざるそば (Zaru soba — chilled soba with dipping sauce [CANONICAL·high])
- English name: Zaru soba (chilled buckwheat noodles served with dipping sauce)
  [CANONICAL·high] (plain/established term; Policy B — Japan-unique dish, Romaji + gloss)
- Components & ingredients:
  - soba noodles (composite → buckwheat flour + WHEAT flour, ratio undetermined)
    [MENU·high] that noodles are present; **flour ratio [UNKNOWN]** ← drives buckwheat
    + wheat allergen; → gap
  - dipping sauce / つゆ (composite → dashi + soy sauce + mirin)  [INFERRED·med]
    - dashi (composite → kombu [INFERRED·med] + katsuobushi/bonito [INFERRED·med];
      possible mackerel/sardine [UNKNOWN])
    - soy sauce (composite → soy + wheat)  [INFERRED·med]
    - mirin  [INFERRED·low]
  - nori / seaweed garnish (commonly on ざる, not かけ)  [INFERRED·med] ← present or not? → gap
  - wasabi + negi (spring onion) as condiments  [INFERRED·med]
- Cooking methods: boil (noodles), then chill/rinse; sauce is uncooked-assembled
  [INFERRED·high]
- Canonical matches applied: glossary/established term for the dish name. No
  product_master beverage match.
- Notes: noodle flour ratio and つゆ exact recipe are the load-bearing unknowns.

## Dish 2 — 天ぷらそば (Tempura soba — hot soba in broth topped with tempura [CANONICAL·high])
- English name: Tempura soba (hot buckwheat noodles in broth, topped with tempura)
  [CANONICAL·high] (established term; Policy B)
- Components & ingredients:
  - soba noodles (composite → buckwheat + WHEAT, ratio undetermined)  [MENU·high] /
    **ratio [UNKNOWN]** → gap (same as Dish 1)
  - hot broth / かけつゆ (composite → dashi + soy sauce + mirin)  [INFERRED·med]
    - dashi (kombu + katsuobushi; possible mackerel/sardine)  [INFERRED·med] /
      mackerel/sardine [UNKNOWN]
    - soy sauce (→ soy + wheat)  [INFERRED·med]
  - tempura (composite, expand):
    - batter (composite → WHEAT flour + EGG + water)  [INFERRED·med];
      **egg in batter? [UNKNOWN]** (some tempura batters use egg, some don't) → gap
    - **tempura item identity [UNKNOWN]** — shrimp (海老天) is the default for
      天ぷらそば, but could be vegetable (kakiage) or mixed → gap. Shrimp would add
      crustacean (JP-mandatory).  [INFERRED·med that it is shrimp]
    - **frying oil [UNKNOWN]** — pure vegetable vs. blend containing sesame/peanut
      oil → drives sesame/peanut allergen → gap
- Cooking methods: boil (noodles), simmer (broth), deep-fry (tempura)  [INFERRED·high]
- Canonical matches applied: established dish-name term. No beverage match.
- Notes: tempura is the highest-risk component — three independent safety unknowns
  (item identity, batter egg, frying oil) plus the shared noodle ratio.

## Dish 3 — カレーうどん (Curry udon — udon in curry broth [CANONICAL·high])
- English name: Curry udon (wheat noodles in Japanese curry broth)
  [CANONICAL·high] (established term; Policy B)
- Components & ingredients:
  - udon noodles (composite → WHEAT flour + salt + water)  [CANONICAL·high] —
    udon is wheat by definition; wheat allergen here is **not** in question
  - curry broth (composite, expand — curry roux is the classic hidden-allergen case):
    - curry roux (composite → WHEAT flour + fat/oil + curry spices + often DAIRY
      (milk powder) + sometimes beef/pork extract)  [INFERRED·med];
      **dairy in roux? [UNKNOWN]** → gap; **animal stock/extract (beef/pork/chicken)
      in roux or broth? [UNKNOWN]** → drives no-beef/no-pork/halal/vegetarian → gap
    - dashi base (kombu + katsuobushi)  [INFERRED·med]
    - **meat topping [UNKNOWN]** — many curry udon include pork or beef or chicken
      or none (plain) → gap
  - negi (spring onion)  [INFERRED·med]
- Cooking methods: boil (noodles), simmer (broth)  [INFERRED·high]
- Canonical matches applied: established term; curry roux expanded as composite per
  data-model rule (allergens hide in roux).
- Notes: curry roux + meat content make this the dish with the most restriction
  (halal/no-pork/no-beef/vegetarian) and dairy unknowns.

## Dish 4 — そばがき (Sobagaki — buckwheat dumpling/porridge [CANONICAL·high])
- English name: Sobagaki (hot buckwheat dumpling — buckwheat flour kneaded with hot
  water)  [CANONICAL·high] (Japan-unique; Policy B — Romaji + gloss)
- Components & ingredients:
  - buckwheat flour + hot water  [INFERRED·high] (sobagaki is, by definition, near-pure
    buckwheat); **is any wheat flour added? [UNKNOWN]** — traditional sobagaki is
    100% buckwheat (wheat-free), but some shops add a little wheat → gap (wheat status)
  - dipping condiment served alongside — possibilities: soy sauce + wasabi, OR
    sugar/kinako, OR つゆ  [UNKNOWN] → affects soy/wheat (via soy sauce) → gap
- Cooking methods: boil/scald-and-knead (湯がき); served hot  [INFERRED·high]
- Canonical matches applied: established Japan-unique term.
- Notes: buckwheat allergen is certain and severe here (highest buckwheat
  concentration on the menu); wheat status depends on whether any wheat is blended in,
  and on what it is dipped in.

---

## Cross-dish summary of decomposition unknowns
- Soba noodle buckwheat/wheat ratio (Dishes 1, 2, and possibly 4) — single biggest gap.
- つゆ / dashi exact composition (soy sauce → soy+wheat; bonito/mackerel/sardine → fish).
- Tempura: item identity (shrimp → crustacean), batter egg, frying oil (sesame/peanut).
- Curry roux: dairy, animal stock/extract; curry udon meat topping.
- Sobagaki: any wheat blended in; what it's dipped in.
