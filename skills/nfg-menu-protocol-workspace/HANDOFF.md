# NFG Menu Protocol — session handoff

**Last updated:** 2026-06-16 · **Status:** skill drafted + 2 eval iterations passed; not yet packaged.

This file lets a new session resume without the prior chat history. Read it, then read
the skill files it points to.

---

## 1. What we're building and why

`nfg-menu-protocol` is a **skill** that models the core of what OmiseAI will eventually
do: turn a restaurant's raw menu (photos / PDF / text) into a verified **NFG (Nicomacos
Food Graph)** dataset, through a numbered, auditable pipeline whose #1 goal is to **never
let an AI guess reach a diner as fact** — especially for allergens.

It's a *manual reference protocol* run by a human-in-the-loop now, intended later to be
the blueprint for an automated multimodal agent harness. The output (stage `06`)
resembles what OmiseAI will store in its database.

Full product context: **`../nfg-menu-protocol/NFG_SUMMARY.md`** (the NFG spec Matt
provided). Project background also in the repo's root `CLAUDE.md`.

## 2. Where everything lives

Repo root: `/Users/matthewchana/Documents/docs` (a Mintlify docs site; `skills/` and
`nfg-runs/` are in `.mintignore` so they don't affect the docs build).

```
skills/nfg-menu-protocol/                 ← THE SKILL (the deliverable)
├── SKILL.md                              ← main protocol (English; the one the agent runs)
├── SKILL.ja.md                           ← Japanese translation for human reading (not executed)
├── NFG_SUMMARY.md                        ← the NFG product/data-model spec (reference)
├── evals/evals.json                      ← the 3 test prompts
├── references/
│   ├── nfg-data-model.md                 ← 8 masters, 32-allergen/5-country, canonical policy
│   └── stage-templates.md                ← markdown templates for each numbered stage file
└── assets/canonical/                     ← canonical "kill-switch" assets (SEED data + schemas)
    ├── README.md                         ← lookup order + matching rules + missing-asset policy
    ├── product_master.json               ← seed (2 entries; prod=244)
    ├── ingredient_glossary.json          ← seed (7 entries; prod=481)
    ├── food_culture_kb.json              ← seed (2 entries; prod=99)
    ├── schemas/*.schema.json             ← shape of each asset
    └── candidates/                       ← human-review queue (kept empty in the bundle)

skills/nfg-menu-protocol-workspace/       ← eval harness + results (NOT part of the skill)
├── grade.py                              ← assertion grader (run: python3 grade.py iteration-N)
├── build_ja_review.py                    ← builds the Japanese review page (python3 build_ja_review.py iteration-N)
├── HANDOFF.md                            ← this file
├── iteration-1/                          ← first eval run (skill BEFORE stage 07 / canonical)
│   ├── review.html (English) · review_ja.html · benchmark.{json,md}
│   └── eval-*/{with_skill,without_skill}/run-1/{outputs,grading.json,timing.json,eval_metadata.json}
└── iteration-2/                          ← second run (skill WITH stage 07 + canonical assets)
    ├── review_ja.html                    ← the current Japanese judging page for Matt's colleague
    └── eval-*/with_skill/run-1/{outputs, outputs_ja, grading.json, ...}
```

## 3. The skill's design (so you don't have to re-derive it)

- **Numbered stage pipeline**, one run per restaurant menu, written to
  `nfg-runs/<slug>/`:
  - `01_source_capture` (verbatim transcription, no interpretation)
  - `02_decomposition` (dishes → ingredients + cooking methods; composites expanded;
    every field provenance-tagged; canonical assets applied here)
  - `03_allergens_restrictions` (allergens DERIVED from ingredients, derivation chain
    shown; inherits weakest provenance in the chain)
  - `04_gap_register` (open questions for the operator, ranked safety-first)
  - `05_operator_dialogue` (gap Q&A — live and/or async; "varies by item" must NOT cascade)
  - `06_nfg_output` (the dataset in NFG shape + verification gate; DRAFT until 07, then finalized)
  - `07_operator_review` (assembled findings shown back to the operator IN JAPANESE for
    sign-off, foregrounding every `[INFERRED]` item with ✔/✖ actions — this is where VAD is earned)
- **Provenance rubric (the core anti-hallucination mechanism):** every claim carries a
  tag — `[MENU] [OPERATOR] [CANONICAL] [INFERRED] [UNKNOWN]` — plus confidence
  `·high|med|low`. **Iron rule:** an `[INFERRED]`/`[UNKNOWN]` claim touching
  allergens/restrictions may never be written as fact; it becomes a gap question.
- **verification_rank** S/A/B/C per dish (S = all safety fields OPERATOR/CANONICAL).
- **Canonical assets** override model guesses; if missing/no-match → degrade to
  `[INFERRED]`→gap, optionally write a `candidates/` draft for human review. **Never
  fabricate canonical data.**

## 4. Eval results so far

3 test cases (in `evals/evals.json`): izakaya full ingest, allergy-trap lunch (tonkatsu/
ebi-fry/annin-dofu/coffee-jelly), gap-finding soba shop. Each run is done with the
operator deliberately "unavailable," to test that gaps stay open and nothing unsafe is
asserted.

- **Iteration 1** (skill before stage 07 + canonical): with-skill **100%** assertion
  pass vs **~48%** baseline (no skill). Verified the safety behavior: only menu-printed
  or canonical allergens asserted; everything inferred routed to gaps; gelatin≠meat;
  杏仁豆腐≠soy; soba buckwheat/wheat ratio surfaced as top gap; sake NOT mis-matched via
  龍-substring.
- **Iteration 2** (skill with stage 07 + canonical assets): with-skill **8/8 on all
  three**. Sake matched `pm_kokuryu_junmai_ginjo` by full identity; no-match dishes
  degraded correctly without fabrication; Japanese stage-07 sign-off sheets produced.

Grading is computed against the English `outputs/`. `iteration-2/*/outputs_ja/` are
human-readable Japanese translations of the outputs for the colleague's review page
(presentation only — they do not affect grading).

## 5. Decisions already made (don't relitigate unless Matt asks)

- Save location: inside this Mintlify repo, under `skills/`, excluded via `.mintignore`.
- Clarification step: BOTH a persisted ranked gap register AND live questioning.
- Run scope: one full menu per run.
- Canonical assets: bundle seeds + schemas; **degrade, never fabricate**; candidates
  queue for human promotion.
- Stage 07 sign-off sheet is written in the operator's language (Japanese for these stores).
- Latin text remaining in the Japanese review page is intentional NFG *data* (provenance
  tags, machine field keys, `name_en`), not untranslated prose.

## 6. Open threads / likely next steps

- **Package the skill** as an installable `.skill` (skill-creator `scripts/package_skill.py`).
  Not yet done.
- Possible SKILL.md adjustments after Matt's colleague reviews `iteration-2/review_ja.html`
  and returns a `feedback.json` (the review page's "評価を書き出す" button downloads it).
- Optional: description-triggering optimization (skill-creator `run_loop.py`).
- Optional: localize provenance tags into Japanese (`[推測]` etc.) — Matt was offered this
  and has not requested it.
- The canonical seeds are tiny; real product_master/ingredient_glossary/food_culture_kb
  would be mounted from the actual project/DB in production.
- Consider whether inferred *restrictions* (not just allergens) should also be held back
  to the gap register rather than appearing in stage 06 (raised in iteration-1 review).

## 7. How to re-run the eval loop (Cowork, with subagents)

1. Edit the skill in `skills/nfg-menu-protocol/`.
2. For each of the 3 evals, spawn a subagent that reads `SKILL.md` and performs the eval
   prompt with "operator unavailable," saving stage files to
   `iteration-N/eval-*/with_skill/run-1/outputs/`. (See `evals/evals.json` for prompts;
   prior subagent prompts are reconstructable from this file.)
3. `python3 grade.py iteration-N` → writes `grading.json` per run; then add a `summary`
   block (see prior pattern) for the benchmark aggregator.
4. To refresh the Japanese review page: translate the new `outputs/` into `outputs_ja/`
   (faithful translation; keep provenance tags / field keys / `name_en`), then
   `python3 build_ja_review.py iteration-N` → `review_ja.html`.
5. The skill-creator tooling lives (read-only) at the plugin skills cache under
   `.../skills/skill-creator/` (`scripts/aggregate_benchmark.py`, `eval-viewer/
   generate_review.py`, `scripts/package_skill.py`).

---

See `KICKOFF_PROMPT.md` (same folder) for a ready-to-paste prompt to start the next session.
