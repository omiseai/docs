# Torihei (鳥平) — Structured Menu Data

**Restaurant:** Torihei — izakaya, Osaka
**Data source:** `live` (new onboarding)
**Purpose:** Structured ingest so the AI concierge can answer diner questions (incl. allergens) about this menu.
**Allergen schema:** NGraph 32-item set; Japan 5-country mapping referenced where confident.

> **Verification note (VAD / HITL):** Everything below is **AI-structured (`verification_rank: ai_generated`)**. It has NOT been confirmed by the owner. Allergen and ingredient fields marked **(confirm)** are best-effort inferences and MUST be owner-verified before the concierge presents them as authoritative. See `torihei_verification_checklist.md`. Verified data, once entered, always outranks these guesses.

---

## Menu items

### 1. 牛すじ煮込み — Gyūsuji Nikomi (Simmered Beef Tendon)
- **id:** `torihei-food-001`
- **category:** 一品 (small plate / appetizer)
- **price:** ¥680
- **translation (en):** Slow-simmered beef tendon stew
- **short_description (en):** Beef tendon simmered until soft in a savory soy-and-miso-based broth, a classic izakaya comfort dish.
- **typical_ingredients (confirm):** beef tendon (牛すじ), soy sauce, miso (often), mirin, sake, sugar, dashi, konnyaku (common), daikon (common), spring onion (garnish), shichimi/togarashi (optional garnish)
- **allergens (confirm):**
  - **soy** — likely (soy sauce / miso) — *confidence: high*
  - **wheat** — likely (soy sauce typically contains wheat; some recipes use miso w/ barley) — *confidence: medium-high — confirm soy-sauce brand*
  - dashi may contain **fish (bonito)** — *confidence: medium — confirm broth base*
- **dietary flags:** NOT vegetarian/vegan (beef). Not halal/kosher unless owner states otherwise.
- **needs_owner_input:** confirm whether miso is used; confirm dashi base (katsuo/bonito vs. kombu); confirm konnyaku/daikon inclusion.

### 2. 鶏の唐揚げ — Tori no Karaage (Japanese Fried Chicken)
- **id:** `torihei-food-002`
- **category:** 一品
- **price:** ¥580
- **translation (en):** Japanese-style fried chicken
- **short_description (en):** Marinated bite-sized chicken (usually thigh), coated and deep-fried until crisp; an izakaya staple, typically served with lemon.
- **typical_ingredients (confirm):** chicken (thigh, 鶏もも), soy sauce, sake, ginger, garlic, potato starch and/or wheat flour (coating), egg (sometimes in batter), frying oil, lemon (garnish)
- **allergens (confirm):**
  - **soy** — likely (marinade) — *confidence: high*
  - **wheat** — likely (soy sauce; coating may include wheat flour) — *confidence: medium-high — confirm coating: katakuriko (starch, wheat-free) vs. flour*
  - **egg** — possible (some batters) — *confidence: low-medium — confirm*
  - frying-oil cross-contact risk if shared fryer with other items — *confirm*
- **dietary flags:** NOT vegetarian/vegan (chicken).
- **needs_owner_input:** confirm coating (starch vs. wheat flour vs. mix); confirm egg in batter; confirm shared-fryer cross-contact.

### 3. だし巻き卵 — Dashimaki Tamago (Rolled Dashi Omelette)
- **id:** `torihei-food-003`
- **category:** 一品
- **price:** ¥480
- **translation (en):** Rolled Japanese omelette cooked with dashi stock
- **short_description (en):** A soft, layered omelette gently rolled and seasoned with dashi, lightly sweet/savory; often served with grated daikon.
- **typical_ingredients (confirm):** egg, dashi (commonly bonito/katsuo + kombu), soy sauce (light/usukuchi), mirin, sugar, salt, oil; grated daikon (common garnish)
- **allergens (confirm):**
  - **egg** — yes (core ingredient) — *confidence: very high*
  - **fish** — likely (bonito dashi) — *confidence: medium-high — confirm dashi base*
  - **soy** — likely (seasoning) — *confidence: medium-high — confirm*
  - **wheat** — possible (via soy sauce) — *confidence: medium — confirm*
- **dietary flags:** vegetarian ONLY if kombu-based dashi and no fish; contains egg (not vegan).
- **needs_owner_input:** confirm dashi base (bonito vs. kombu) — this is the decisive vegetarian/fish-allergen factor.

### 4. ポテトサラダ — Potato Salad
- **id:** `torihei-food-004`
- **category:** 一品
- **price:** ¥380
- **translation (en):** Japanese-style potato salad
- **short_description (en):** Creamy mashed-potato salad bound with mayonnaise, usually with cucumber, onion, carrot, and ham.
- **typical_ingredients (confirm):** potato, Japanese mayonnaise (egg yolk, vinegar, oil), cucumber, onion, carrot, ham (common), salt, pepper; sometimes corn
- **allergens (confirm):**
  - **egg** — likely (mayonnaise) — *confidence: high — confirm mayo type*
  - **pork** — possible (ham) — *confidence: medium — confirm ham inclusion*
  - **soy** — possible (mayo / ham seasoning) — *confidence: low-medium*
  - **milk** — possible (some recipes) — *confidence: low — confirm*
- **dietary flags:** NOT vegan (mayo/egg); vegetarian only if no ham — confirm.
- **needs_owner_input:** confirm ham inclusion (affects vegetarian + pork allergen); confirm mayonnaise (egg).

### 5. 本日の刺身盛り合わせ — Honjitsu no Sashimi Moriawase (Today's Assorted Sashimi)
- **id:** `torihei-food-005`
- **category:** 一品 (chef's daily selection)
- **price:** ¥1200
- **translation (en):** Assorted sashimi platter (chef's daily selection)
- **short_description (en):** A chef-selected assortment of fresh raw fish/seafood that changes daily; served with soy sauce, wasabi, and shiso/daikon garnish.
- **typical_ingredients (confirm — VARIABLE DAILY):** assorted raw fish/seafood (varies daily — e.g., tuna/maguro, salmon, yellowtail/buri, sea bream/tai, squid/ika, shrimp/ebi, etc.), soy sauce, wasabi, daikon tsuma, shiso (accompaniments)
- **allergens (confirm — VARIABLE DAILY):**
  - **fish** — yes (core) — *confidence: very high*
  - **shellfish/crustacean** (shrimp) and **mollusc** (squid) — possible depending on the day's selection — *confidence: medium — VARIES DAILY*
  - **soy / wheat** — likely (accompanying soy sauce) — *confidence: medium-high*
- **dietary flags:** NOT vegetarian/vegan (raw fish/seafood); raw item.
- **needs_owner_input:** **CRITICAL** — because the contents change daily, the concierge must NOT assert a fixed allergen list. The owner should provide today's fish list (ideally daily) or the concierge must tell diners "ask staff for today's selection." This item is the highest allergen-risk item on the menu.

---

## Drinks

### 6. 黒龍 純米吟醸 (グラス) — Kokuryū Junmai Ginjō (Glass)
- **id:** `torihei-drink-001`
- **category:** 酒 (sake / nihonshu)
- **price:** ¥900 (by the glass)
- **translation (en):** Kokuryu Junmai Ginjo sake, served by the glass
- **brewery:** Kokuryu Sake Brewery (黒龍酒造), Fukui Prefecture
- **type:** Junmai Ginjo (pure-rice ginjo) sake
- **short_description (en):** A refined junmai ginjo from a renowned Fukui brewery — clean, fragrant, and balanced; pairs well with sashimi and lighter izakaya dishes.
- **allergens:** none of the 32 schema items typically apply to pure-rice sake (rice, water, koji, yeast). Alcohol — flag for diners avoiding alcohol.
- **product_master note:** Kokuryu is a well-known brewery and a strong candidate for a verified `product_master.json` entry. **Do NOT let the concierge free-generate tasting notes / specs.** Pull verified brewery specs (rice polishing ratio, etc.) into product_master and serve from there; otherwise show only the grounded fields above. Confirm exact SKU/grade with owner (Kokuryu has several junmai ginjo products).
- **needs_owner_input:** confirm exact product label/grade; provide verified spec for product_master so concierge does not hallucinate tasting notes.

---

## Source fidelity notes
- Prices, names, and categories are transcribed **exactly** from the owner-supplied menu. These are reliable.
- "本日の" (today's) on the sashimi means daily-variable contents — treat as a template, not fixed data.
- All ingredient/allergen fields are AI inference from typical izakaya recipes and are **unverified guesses** until the owner confirms. Per VAD rules, the concierge must surface uncertainty on allergen answers and defer to staff for the sashimi platter.
