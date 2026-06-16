# Soba Shop Onboarding — Owner Verification Questions

**Goal:** Identify what the AI concierge cannot safely answer about these four dishes until the owner confirms (VAD — Verified Authentic Data). Until each item below is owner-confirmed, the concierge must not free-generate answers; verified data outranks AI guesses (`verification_rank`).

## Menu under review

| Dish | Price | What the AI can guess | What it must NOT guess |
|---|---|---|---|
| ざるそば (zaru soba) | ¥700 | Cold buckwheat noodles, dipping tsuyu | Buckwheat % vs. wheat; gluten/wheat content; tsuyu ingredients |
| 天ぷらそば (tempura soba) | ¥1,100 | Soba in hot broth with tempura | Which tempura (shrimp? vegetable?); shellfish; batter; broth base |
| カレーうどん (curry udon) | ¥950 | Wheat udon in curry broth | Meat type; dashi base; roux/allergen contents; spice level |
| そばがき (soba-gaki) | ¥600 | Buckwheat dumpling/porridge | How served; accompaniments; buckwheat purity |

---

## CRITICAL — Allergen safety (must verify before launch)

Soba is one of the most allergy-sensitive cuisines in Japan. Buckwheat (そば) is a designated severe-allergen item in Japan, and these dishes almost certainly involve cross-contamination and hidden allergens. We map allergens across our 32-item, 5-country schema, so every answer below feeds that.

1. **Buckwheat / wheat ratio in the soba.** Is your soba "juwari" (100% buckwheat) or a blend (e.g., nihachi 80/20)? Diners ask both "is this gluten-free?" (buckwheat itself is gluten-free) and "does it contain buckwheat?" (severe allergy). We must NOT guess the ratio — getting this wrong is dangerous in both directions.
2. **Does the udon kitchen share equipment / water with the soba?** Buckwheat cross-contamination into the curry udon (and vice versa wheat into soba) is the #1 question a buckwheat-allergic diner will ask. Need: shared pots, shared boiling water, shared cutting boards?
3. **Tsuyu / broth (dashi) base for each dish.** Almost all soba tsuyu contains: bonito (katsuobushi — fish), kombu, soy sauce (wheat + soy), mirin, sometimes mackerel/sardine. Confirm exact base for (a) zaru tsuyu, (b) tempura soba hot broth, (c) curry udon broth. This drives fish / shellfish / wheat / soy allergen flags.
4. **Tempura soba — what is the tempura?** Shrimp (ebi)? Vegetable (kakiage)? Mixed? This is a shellfish-allergen and a price-justification question. Also: is the batter wheat-based (yes, normally) and is it fried in oil shared with shellfish?
5. **Curry udon — meat and broth.** Pork? Beef? Chicken? None (vegetarian)? Critical for halal/vegetarian/religious-restriction diners and for the dashi question (does the "curry" broth contain fish dashi — a hidden non-vegetarian/fish allergen?).
6. **Curry roux composition.** Commercial Japanese curry roux frequently contains wheat flour, milk solids, and sometimes apple/honey. Confirm: house-made or commercial roux, and which one (so we can read its allergen label).
7. **Soba-gaki accompaniments.** Served with soy sauce / wasabi / nori / sugar+kinako? Each adds allergen flags (soy, wheat in soy sauce).

---

## Ingredient / canonical-data questions (for NFG + cross-language accuracy)

8. **Soba-gaki — what exactly is it and how is it served here?** This is an uncommon dish many foreign diners won't recognize. Is it the warm kneaded buckwheat dumpling (eaten with tsuyu/wasabi) or the looser porridge style? We need the owner's actual preparation to write the 28-language description and cultural context — not a generic dictionary definition.
9. **Is the soba house-made (teuchi) or supplied?** Affects buckwheat-purity claims and the authenticity narrative.
10. **Curry udon noodle.** Confirm it's wheat udon (vs. soba) — the name implies udon but worth confirming there's no soba option, for the buckwheat-allergy story.
11. **Wasabi: real (hon-wasabi) or horseradish-based imitation?** Common diner question; affects ingredient/canonical entry.

---

## Pricing / portion / availability questions

12. **Is tempura soba served hot only, or is a cold (tempura + zaru) version available?** Diners will ask; we should not assume.
13. **Any seasonal or sold-out limits** (e.g., soba-gaki made to order, limited daily quantity)?
14. **Spice level of curry udon** — fixed, or adjustable? Common diner question.
15. **Vegetarian/vegan options.** Given dashi is fish-based, can any of these four be made vegetarian on request? If "no," the concierge should state that clearly rather than guess.

---

## Why this matters (grounding rule)

Per our design principles, the concierge **grounds every answer in confirmed DB data**. For a soba shop the failure mode is severe: a buckwheat- or shellfish-allergic diner relying on a hallucinated "gluten-free" or "no shellfish" answer. Until items 1–7 are owner-verified (VAD), the concierge should respond to allergen and dietary questions with "let me confirm with the restaurant" rather than generate an answer.
