# Question Engine — Specification

Last updated: 2026-06-06 / Status: Draft (in implementation)
English translation of `QUESTION_ENGINE_SPEC.md` (Japanese original is the source of truth).

The canonical ruleset for generating "AI confirmation items" for restaurant owners, channel-independent (admin UI / LINE). LINE is only a delivery channel; this document fixes **what to ask and how to prioritize**.

---

## 0. Design philosophy

- Don't ask for the data you want to collect — ask only the **minimum needed to kill the AI's uncertainty**.
- Questions are confirmations, not data entry: not "please enter X" but "**the AI judged it this way — is that right?**"
- Stop at the granularity of **facts the owner can answer instantly from memory**. Anything beyond that (allergen derivation, etc.) is computed by the knowledge base, not asked.
- For safety items, prefer an honest "**unknown**" over a false "none" (makoto / making the NFG "don't write what you can't verify" stance explicit and safe).
- Development decision criterion: **does this feature reduce the owner's taps?** If not, lower its priority.
- **All owner-facing text (question body, options, button labels) must be polite Japanese (teineigo). No casual speech.** e.g. ○「合っていますか？」「わかりません」「含みます」 / ✗「合ってる？」「わからない」「含む」.

---

## 1. Priority tiers (owner-facing)

Internal rank (S/A/B/C) is never shown to the owner. Display is 3 categories.

| Tier | Display name | Targets | Save fields |
|---|---|---|---|
| `safety` | Check before publishing | allergens / alcohol / pork-derived / beef-derived / raw / religious constraints | `allergens` / `restrictions` / `cooking_methods` / `is_alcoholic` |
| `order` | Affects ordering decisions | spiciness / portion / kid-friendly / limited item / availability | `taste_values` / `serving` / `featured_tags` / `status` |
| `appeal` | Boost appeal | pairing / how to eat / chef's care / story | `narrative` (pairing_suggestion / chef_note / story etc.) |

- `safety` is **never capped** (top priority, always kept). Count caps apply to `order` / `appeal` only.
- Sort: `safety` → `order` → `appeal`; within each tier, descending priority score.
- **Don't blanket-skip beverages.** Sake/beer/wine get `safety` (alcohol confirmation) for ABV / minors / pregnancy / religion. Soft drinks and food-only items are filtered by scope (`applies_to`: food/drink).

---

## 2. Question-format selection (the core)

Presenting a single low-confidence assertion makes owners rubber-stamp it ("eh, close enough" = acquiescence bias). **Vary the format by confidence band.**

| Condition | Format | Example |
|---|---|---|
| Safety item, value present (any confidence) | **Confirm (editable)** | "Allergens are 【wheat・egg】, correct?" — checks can be added/removed |
| Safety item, no value | Enumerate (don't assert) | "What's the dressing on this salad?" |
| Non-safety, confidence ≥ 0.85 | **Don't ask** (trust) | — |
| Non-safety, 0.55 ≤ confidence < 0.85 (close) | **Confirm** | "Spiciness is 'medium', correct? 1. Right 2. Fix" |
| Non-safety, confidence < 0.55 (split) | Enumerate (don't assert) | pick from candidates |

Threshold constants: `CONFIDENCE_CONFIRM_HIGH = 0.85` / `CONFIDENCE_CONFIRM_LOW = 0.55` (pending approval, tunable).

Confirm-type options always include a **common exit** (the engine MUST output these as the question object's `actions` — never leave it to the adapter):
1. Correct / 2. Wrong (fix) → falls back to enumeration on the spot / 3. Not applicable (e.g. this dish uses no dashi) / 4. Don't know (→ §4 unknown terminal)
- Enumeration (select/multi) gets "Not applicable / Don't know"; item_confirm gets "Correct / Fix".

---

## 3. Three-step depth escalation (stop as shallow as possible)

| Step | What's asked | Example | Terminal |
|---|---|---|---|
| L1 store-common | products/methods in use (existing `kitchen_profile.py`) | "What's your main dressing?" | CASCADE settles ~80% |
| L2 per-item exception | when only this dish differs (1-tap confirm) | "Is only this salad house-made?" | settled |
| L3 house-made/varies/unknown | the **ingredients** inside (never ask by allergen name) / if commercial, **photograph the ingredient label** → Vision OCR | "What's in the house-made dressing?" | settled or unknown |

**Never make allergens a question (including confirm-type).** Even "Allergens are 〜, correct?" is banned — owners can't connect "fish = from the dashi". The owner only answers "what do you use (the fact = ingredients)". Allergens are **derived** by the knowledge base (ingredient master `allergen_flag` / CASCADE); the final check is **display only** at the publish gate (§5).

Instead, ask **ingredient-axis questions**, narrowing options via store-common answers:
- e.g. (dashimaki tamago): ✗ "Allergens are egg・fish, correct?" → ◯ "What's the dashi in this dish? 1. Bonito/niboshi 2. Kombu 3. Shiitake 4. Other" → bonito derives fish.
- If store-common already says "our dashi = bonito only", the per-item simplifies to "1. Bonito 2. Other", or inherits → **zero questions**.
- Structured ingredient-axis questions (dashi/batter/oil…) are owned by **`kitchen_profile`** (it holds the ingredient vocabulary and CASCADE). `question_engine` only holds the generic fallback when ingredients are wholly unknown ("tell us the main ingredients / photograph the label").

> ⚠ Known gap: `kitchen_profile`'s dashi CASCADE scope is category-dependent on `{soup,nabe,steamed,rice,soba}`, so **dashimaki tamago (side) is missed even though its name contains "dashi"** → fish isn't auto-assigned. Cover with a per-item ingredient-axis question (or judge scope by keyword too).

---

## 4. State model (generate ⇄ answer ⇄ write-back ⇄ re-ask suppression)

Generation rules alone aren't enough. Post-answer state lives in `field_confidence` (JSON column, **no migration needed**).

### field_confidence convention (after unification)

```jsonc
{
  // existing: per-field confidence 0.0–1.0
  "allergens": 0.7, "ingredients": 0.5, "cooking_methods": 0.4, ...,
  // field names confirmed by owner/first-party source (present/absent/complete confirmed)
  "verified_fields": ["allergens", "dashi"],
  // terminal fields the owner confirmed as "don't know" (don't re-ask; show as unverified to diners)
  "unknown_fields": ["gelatin"],
  // per-item tri-state for designated allergens (§5)
  "allergen_status": { "egg": "unknown", "wheat": "present", "milk": "absent" }
}
```

> ⚠ Unify existing inconsistency: collapse the **two systems `verified_fields` (confidence.py) and `store_verified` (kitchen_profile.py) into one `verified_fields`**. CASCADE pushes the **confirmed field name** (e.g. `allergens`) into `verified_fields`, not a coarse "kitchen_profile" tag. → Without this fix, allergens filled at store-common level get re-asked per-item (double-question bug).
> **In Phase 1, don't trust `store_verified`.** The old tag only means "CASCADE ran", not "that field was confirmed". Normalizing old data into `verified_fields` happens in the Phase 2 migration.

### Answer → write-back map

| Answer | Write-back | Re-ask |
|---|---|---|
| Correct / Fixed | update value + add to `verified_fields` + rank promotion | no |
| Not applicable (confirmed empty) | clear value + add to `verified_fields` ("verified empty") | no |
| Don't know | add to `unknown_fields` (keep AI guess as reference) | no (terminal) |

`verification_rank`: unify to `C` (AI guess/unverified) → `B` (owner confirmed) → `A/S` (first-party source).
> ⚠ Existing inconsistency: `confidence.py` treats `C` as "confirmed", `kitchen_profile.py` treats `C` as "unverified" — **opposite**. Unify to `C = unverified`.

---

## 5. Allergen special rules (safety, highest priority)

Allergens are frequently unknown even to the owner (supply source, OEM, ready-made sauces), and **rounding "unknown" to "none" causes incidents** (direct liability). Hence special handling.

- **Tri-state, not binary (present/absent)**: `present` / `absent` / `unknown` (per the 8 designated allergens).
- **Default for empty value is `unknown`, not `absent`.** When empty, don't force the owner to assert a negative ("none, correct?") — the mayo/dressing problem. Present values get a confirm-type review of the derived result; empty is resolved by ingredients or a photo of the label (L3). `absent` only when the owner explicitly denies it.
- Vary the diner-facing AI response by state:
  - present → "Contains egg"
  - absent (owner-confirmed) → "Does not use egg"
  - **unknown → "Not yet confirmed. Please check with the restaurant/staff"** (NEVER let it say "does not contain")
- **Remove `confidence.py`'s "verified with empty allergens = perfect safety score".** Dishes with remaining unknowns don't get a perfect score.
- **Publish gate**: do **not block** publish on unknown allergens (OEM-heavy stores could never publish). **Allow publish but surface "unverified" to diners.** This is the safety-vs-usability balance point.
- Don't let unknown be a dead end: choosing "don't know" → "**send a photo of the ingredient label**" → existing `analyze_image` (Vision) OCRs the ingredient panel → promotes unknown to confirmed.

---

## 6. Five firing conditions (triggers that generate a question)

| # | Trigger | Format | Notes |
|---|---|---|---|
| 1 | Safety item unverified | value present = confirm / no value = enumerate | safety is exempt from cap |
| 2 | Low confidence | decided by §2 band | askable fields only |
| 3 | Conflicts with store-common | confirm | e.g. "Is only this ramen tonkotsu?" Without persisted candidate distribution, currently limited to name/category heuristics (strengthened in a separate job) |
| 4 | Frequent in usage logs | confirm/select | fires after N diner questions (default 5). Needs a separate multilingual-classification job; only works after traffic |
| 5 | New daily special | **item_confirm** (§7) | right after photographing |

---

## 7. Daily specials (item_confirm)

Not per-field but whole-dish-identity confirmation type `item_confirm`.

```
photo → AI structuring → "Today's set is this, correct? (saba miso / small dish / miso soup / rice)"
   → 1. Correct / 2. Fix
   → YES: auto-inherit store-common profile (CASCADE) → ask only exceptional safety items → publish
```

> ⚠ Inheritance caveat: daily specials often use "different oil/dashi than usual". **Store-common auto-inheritance defaults ON but assumes override.** Inherited values are NOT pushed to `verified_fields` — treated as "AI-inherited" (safety items confirmed later via confirm-type).

---

## 8. Question object (channel-independent schema)

```jsonc
{
  "key": "allergens:<menu_uid>",      // stable dedup key
  "menu_uid": "...", "menu_name": "Saba Miso Set",
  "tier": "safety",                    // safety | order | appeal
  "target_field": "allergens",
  "format": "confirm",                 // confirm | select | multi_select | text | item_confirm
  "question": "Are the allergens for 'Saba Miso Set' 【wheat・egg】, correct?",
  "ai_guess": ["wheat", "egg"],        // current value shown in confirm-type (null if none)
  "options": [{"value":"egg","label":"egg"}, ...],  // for enumeration/editing (null if unneeded)
  "actions": [{"value":"correct","label":"Correct"}, ...],  // common exit (§2); engine always outputs
  "allow_photo": true,                 // whether to accept a photo (e.g. ingredient label)
  "trigger": "safety_unverified",      // §6
  "priority": 100.0                    // higher = first
}
```

The LINE side just reformats this into "1 message = 1 question, max 4 options, free text as last resort" and delivers it.

---

## 9. Implementation phases

- **Phase 1 (this spec)**: `question_engine.py` (pure logic, channel-independent, no DB migration). Generation rules + format selection + tiers + 5 triggers. Complete safety items; order/appeal only where a box already exists.
- **Phase 2**: answer → write-back handler (save `verified_fields`/`unknown_fields`/`allergen_status`). Remove confidence.py's "verified-empty = perfect" + unify rank `C` + collapse `store_verified` → `verified_fields`.
- **Phase 3**: publish gate (unknown → diner-facing "unverified"). Change diner-facing AI's unknown responses.
- **Phase 4**: daily-special item_confirm flow + ingredient-label OCR promotion.
- **Phase 5**: LINE delivery adapter (existing `feature/line-bot-phase1`).
- **Phase 6**: Layer3 usage-log analysis job (multilingual classification) + strengthen trigger ③ conflict detection (persist candidate distribution).

Separate task: centralize allergen-derivation knowledge from hardcoded CASCADE_RULES into the ingredient/product master (`allergen_flag` / `product_master` extension).

---

## Appendix: ingredient allergen_flag operating rules (fixed 2026-06-06)

`ingredients.allergen_flag` (comma-separated lowercase tokens) holds ingredient→allergen; dishes derive from ingredients (§3). On 2026-06-06, 593 high/mid-frequency terms were loaded (incl. 247 explicit "none"). Reached: 68% allergen detection / 48% all-ingredient resolution.

**Iron rule: never turn "unknown" into `none`.**
- `none` = "confirmed, no allergen" (can assert "does not contain X")
- unclassified (empty) = "unknown" (→ owner confirmation/photo OCR)
- e.g. `出汁/だし/つゆ` (dashi/broth) may be kombu or shojin dashi, so **leave unclassified — neither fish nor none**. Asserting bonito dashi as `none` = fish-allergy incident. Only named fish dashi (`niboshi/bonito dashi/ago dashi`) gets `fish`.
- Don't infer composite allergens from dish names (`hamburg → beef` only, `curry → unclassified`). Egg/milk/wheat etc. derive from actual ingredients.

**Implemented (2026-06-06): confidence on allergen_flag.**
- Format: embed token:confidence in the `allergen_flag` string. **Bare token = 1.0 (definitional)** / **`:value` = probabilistic**. e.g. `egg`(=1.0) / `soy,wheat`(=1.0) / `fish:0.3` / `wheat:0.5,milk:0.4`. No DB migration.
- Existing data: bare tokens = all 1.0 (backward compatible). `kitchen_profile.allergen_has_ingredient_source` strips `:confidence` before comparing.
- Derivation `allergen_derivation.derive_from_ingredients` returns token→confidence (max across ingredients), split by `split_confidence(hi=0.8)` into **confident (≥0.8: assertable to diner)** and **hypotheses (<0.8: owner confirmation)**.
- `question_engine.build_hypothesis_questions` turns hypotheses into confirm questions ("Does 'X' contain wheat? AI judged it possible"). Confirmed allergens aren't asked.
- This keeps ambiguous dashi from being dropped as "unclassified" — held as `fish:0.3` and routed to confirmation (the precise solution to "unknown ≠ none"). Loaded examples: `dashi→fish:0.3` / `washoku dashi→fish:0.4` / `curry→wheat:0.5,milk:0.4` / `hamburg→beef:0.7,egg:0.5,milk:0.4,wheat:0.5`.
- ⚠ **Diner-facing consumer (Phase 3) must respect confidence**: assert only confident; show hypotheses as "possibly / needs confirmation". Never treat a raw flag as present.

### ★ Governance (most important, fixed)
**allergen_prior (ingredient→allergen prior probability/class) is NOT a confirmed value.** It's a prior for deciding the question engine's "firing / priority / format" — **not used in diner-facing answers**. The only thing presentable to diners is the **owner-confirmed `allergen_status` (present/absent/unknown)**. Asserting "contains" from a raw prior is forbidden.

### Confidence expression: class, not numbers (policy shift 2026-06-06)
Numbers (0.98 etc.) are fake precision nobody measured. OMISEAI's goal isn't probability computation but "what to ask the owner", so **class is the primary expression**. Class is decided by **basis (why the allergen was judged present)**:

| class | confidence band (approx) | basis | question policy |
|---|---|---|---|
| `direct` | 0.95–1.0 | ingredient_direct (the word itself is the ingredient: egg/wheat/shrimp/soy sauce/panko) | generally don't ask (safety may confirm lightly once) |
| `high` | 0.8–0.95 | ingredient_high (mayo/cheese/butter) | confirm lightly |
| `dish_prior` | 0.4–0.75 | dish_prior (hamburg/curry/gratin) | confirm (select or confirm-type) |
| `ambiguous` | 0.2–0.5 | ambiguous (dashi/tsuyu/miso soup/sauce) | don't ask alone; fire when combined with usage logs etc. |
| `none` | 0 | — | don't ask (confirmed absent) |

- Storage: attach class to `allergen_flag` tokens. Bare = `direct`, `token:high` / `token:dish` / `token:amb`; `none` unchanged. e.g. `miso soup → soy,fish:amb` (miso = direct, dashi = ambiguous).
- Future: once owner-confirmation data (YES rate) accumulates, promote class → learned confidence. **For now class; numbers when data arrives.**
