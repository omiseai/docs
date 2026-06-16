# Question Engine — Skill-ification Source Set

> For Matt. The minimal, high-signal set for turning the Question Engine (generating "AI confirmation items" for restaurant owners) into a Claude Code skill.
> Designed so "design philosophy + implementation behavior + safety constraints" are all present in one place.

## Important distinction
The **skill's documentation** is English (this set). The **questions the engine emits to owners stay Japanese** — `QUESTION_ENGINE_SPEC` mandates polite Japanese for owner-facing text, because the owners are Japanese. Don't translate the emitted questions.

## Contents

| File | Layer | Role |
|---|---|---|
| `QUESTION_ENGINE_SPEC_EN.md` | Design / canonical | **Read this first.** What to ask and how to prioritize: 3 tiers (safety/order/appeal), confirm-type questions, confidence bands, allergen tri-state rules, allergen_flag governance |
| `QUESTION_ENGINE_SPEC.md` | Design / canonical (source) | Japanese original — the source of truth the EN version is translated from |
| `kitchen_profile.py` | Implementation core | Store-common questions (13-axis CASCADE). The core of priority queue delivery. Code; comments are in Japanese |
| `question_knowledge.py` | Implementation core | Learning loop: generation reads past answers / purges per-item questions. The "varies" iron rule. Code; comments in Japanese |
| `06_section4_iron_rules_EN.md` | Safety constraints | Allergen-safety and "varies never cascades" — the constraint layer the engine must obey (excerpt of NFG spec §4) |

## Sources (re-copy from here when originals change — these are copies, not links)

- `QUESTION_ENGINE_SPEC.md` ← `C:\dev\ngraph\docs\QUESTION_ENGINE_SPEC.md`
- `kitchen_profile.py` ← `C:\dev\ngraph\NGraph-backend\app\admin_api\kitchen_profile.py`
- `question_knowledge.py` ← `C:\dev\ngraph\NGraph-backend\app\owner_integration\question_knowledge.py`
- `06_section4_iron_rules_EN.md` ← `matt-handover/06_NFG_SPECIFICATION.md` §4

## Optional additional sources (pull in if needed)

- `ngraph/docs/ngraph-hearing-logic.md` — hearing-logic design (389 lines)
- `ngraph/NGraph-backend/app/admin_api/dish_hearing.py` — per-dish hearing
- `*_i18n.py` (kitchen_profile_i18n / dish_hearing_i18n) — question multilingualization
- `ngraph/NGraph-backend/scripts/_e2e_kitchen_chat.py` — E2E test = working spec by example
- `NGraph-front-end/src/components/OwnerQuestionFlow.tsx` — owner-side UI flow

## Note on the .py files
Code is universal, but `kitchen_profile.py` and `question_knowledge.py` have Japanese comments and string literals (owner-facing question text). If full English readability is needed, we can add an English walkthrough doc rather than editing the code.
