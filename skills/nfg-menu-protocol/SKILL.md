---
name: nfg-menu-protocol
description: >-
  Turn a restaurant's raw menu (photos, PDFs, spreadsheets, or pasted text) into
  a verified NFG (Nicomacos Food Graph) dataset through a numbered, auditable
  pipeline that refuses to guess about anything that could harm a diner. Use this
  skill whenever you are onboarding or re-verifying a restaurant's menu for OmiseAI
  / NGraph, decomposing dishes into ingredients and cooking methods, deriving
  allergens or dietary/religious restrictions, preparing operator clarification
  questions, or producing a dish record that conforms to the NFG data model.
  Trigger it for requests like "ingest this menu", "build the NFG data for this
  restaurant", "what do we need to ask the owner about these dishes", "verify the
  allergens for this menu", or any task where menu meaning must be captured
  faithfully enough that an AI concierge can answer "does this dish contain
  peanuts?" without hallucinating. This is the manual reference protocol that the
  future OmiseAI agent harness will automate — follow it exactly so the output
  resembles what we will store in the database.
---

# NFG Menu Protocol

## Why this exists

OmiseAI's concierge answers diner questions — including allergy questions — from
the NFG dataset. If the dataset says a dish is peanut-free and it isn't, someone
gets hurt. So the job is **not** "describe the menu." The job is to build a record
where every safety-relevant claim is traceable to a trustworthy source, and every
unknown is *visible as an unknown* rather than smoothed over by a plausible guess.

A single, well-prompted model call will occasionally invent an ingredient, an
allergen status, or a sake spec. We cannot prompt our way out of that. Instead we
make invention *structurally hard*: we separate what was observed from what was
inferred, we derive allergens mechanically from ingredients, we let verified
canonical data override model output, and we route every gap to a human before it
can become a fact. This protocol is that machine, written out by hand so we can run
it manually now and automate it later.

The guiding principle (from NFG philosophy): the mean between hallucination and
empty fields is **verified, confidence-graded data**. Ship partial data honestly
rather than complete data dishonestly.

## What a run produces

One run handles **one full restaurant menu** and writes a numbered set of markdown
files into a per-restaurant run folder:

```
nfg-runs/<restaurant-slug>/
├── 01_source_capture.md         faithful transcription of every input, no interpretation
├── 02_decomposition.md          dishes → ingredients + cooking methods, every field provenance-tagged
├── 03_allergens_restrictions.md allergens & restrictions DERIVED from ingredients, with the chain shown
├── 04_gap_register.md           open questions for the operator, ranked safety-first
├── 05_operator_dialogue.md      the gap Q&A exchange (asked live and/or answered async)
├── 06_nfg_output.md             the dataset conforming to the NFG model — DRAFT, then finalized
└── 07_operator_review.md        the assembled findings shown back to the operator for sign-off (VAD)
```

The numbering is the process order. Never skip ahead — stage N depends on stage
N-1 being honest. There are **two** operator touchpoints, and they are different:
Stage 05 asks targeted questions to fill specific gaps; Stage 07 shows the operator
the *whole assembled picture* and asks them to confirm or correct it — especially
everything we could only infer. `06_nfg_output.md` is "the output" (the thing that
resembles what we store in the database); it starts as a **draft** and is finalized
only after the Stage 07 sign-off.

Create the folder yourself at the start of a run. Slugify the restaurant name
(e.g. "Bonta 西梅田店" → `bonta-nishi-umeda`). If the user is just exploring with a
single dish, you may still run the full pipeline on that one dish — the stages
scale down.

## The provenance rubric — the heart of this skill

Every factual claim about a dish (an ingredient, a cooking method, an allergen, a
spec) carries a **provenance tag** and a **confidence**. This is what stops
hallucination from reaching a diner. Tag claims inline like `… peanuts [INFERRED·low]`.

| Tag | Meaning | Trust |
|---|---|---|
| `[MENU]` | Printed on the source menu / written in the source material | High |
| `[OPERATOR]` | Confirmed first-hand by the restaurant operator (this is VAD) | Highest |
| `[CANONICAL]` | Matched to a verified asset (product_master, ingredient_glossary, food-culture KB) | Highest |
| `[INFERRED]` | The model's best guess from culinary norms — **not verified** | Low |
| `[UNKNOWN]` | Genuinely undetermined | None |

Confidence is `high` / `med` / `low`, reflecting how sure you are *within* that
source (e.g. a smudged menu photo might be `[MENU·med]`).

**The iron rule that makes the whole thing safe:**

> An `[INFERRED]` or `[UNKNOWN]` claim that affects allergens, dietary
> restrictions, or religious restrictions may **never** be written into the final
> dataset as fact. It must instead become a question in the gap register. Inference
> is fine for narrative flavor text; it is forbidden for safety fields.

So "tonkatsu is breaded, so it likely contains wheat and egg" is a reasonable
inference — but until the operator confirms the breading and the frying oil, the
wheat/egg/soy status is a *gap question*, not a dataset fact. When in doubt about
whether a field is safety-relevant, treat it as if it is.

## Canonical assets — where to look, and what to do if they're missing

The `[CANONICAL]` tag is only honest when it points at genuinely verified data.
This skill bundles the canonical assets (and their schemas) under
`assets/canonical/`:

- `product_master.json` — verified beverage/product specs (sake, shochu, wine…)
- `ingredient_glossary.json` — verified English ingredient names + the boundary rule
- `food_culture_kb.json` — verified regional-dish cultural narratives

At the start of a run, look for these. In production they may instead live at a
project path or be served from the database — if the user points you at a fuller
copy, prefer it. Read `assets/canonical/README.md` for the lookup order and the
matching rules (including the 龍 ⊂ 黒龍 substring trap).

**What to do when an asset is missing, or a dish doesn't match any entry — this is
the important part:** do **not** invent canonical data to fill the hole. Fabricated
"canonical" data is the worst possible failure here, because it launders a guess
into something that looks verified and outranks everything. Instead:

1. Treat the unmatched fact as `[INFERRED]` (or `[UNKNOWN]`) and let the normal
   safety rule apply — if it touches allergens, it becomes a gap question.
2. You *may* propose a **candidate** entry — your best draft of what the canonical
   record might be — by appending it to `assets/canonical/candidates/<asset>.candidates.jsonl`
   with a `status: "draft-unverified"` field. Candidates are explicitly **not**
   canonical; they're a queue for a human to verify (against the brewery spec, the
   glossary, the MAFF source) and promote. This mirrors the meta-rule for all
   AI-generated canonical data: **AI generates → human reviews the diff → apply.**

Never read your own candidates back as `[CANONICAL]` within the same run.

## Stage-by-stage

Read `references/stage-templates.md` for the exact markdown shape of each file, and
`references/nfg-data-model.md` for the enumerations you must map onto (the 8
masters, the 32-item/5-country allergen list, the 12 restrictions, cooking methods,
canonical-asset policy). Pull these in as you reach the stage that needs them
rather than loading everything up front.

### Stage 01 — Source capture (`01_source_capture.md`)
Transcribe everything you were given, verbatim, in the original language, with no
interpretation. Photos, PDF text, spreadsheet rows, pasted text — all of it. Record
each menu item's printed name, any printed description, price, and section. Note the
medium and quality of each source ("photo, slightly blurry, lower-left dishes hard
to read"). If you genuinely cannot read something, write `[illegible]` — do not
guess at it. This file is the ground truth of *what we actually received*; later
stages are judged against it.

### Stage 02 — Decomposition (`02_decomposition.md`)
For each dish, break it into components and then ingredients, mapping onto the NFG
ingredient model (simple / composite-with-`components` / processed). A composite
ingredient like curry roux expands to flour + fat + beef + dairy — expand it,
because allergens hide inside composites. Assign cooking methods from the 20-method
list. **Tag every single field** with provenance + confidence. Apply the canonical
assets here: if a dish or beverage matches `product_master` or a term is in
`ingredient_glossary`, mark it `[CANONICAL]` and use the canonical value — it
overrides any inference. Follow the glossary boundary rule (plain English when one
exists; Romaji+gloss only for Japan-unique items). Anything you're filling from
culinary knowledge rather than the source is `[INFERRED]`; anything missing is
`[UNKNOWN]`.

### Stage 03 — Allergens & restrictions (`03_allergens_restrictions.md`)
Allergens are **derived from ingredients, never tagged ad hoc.** For each dish, walk
its ingredient list (including expanded composite components) and show the
derivation chain: which ingredient implies which allergen, across the 32-item
5-country mapping. Do the same for the 12 dietary/religious restrictions. The
derived allergen status inherits the **weakest** provenance in its chain — if the
breading is `[INFERRED]`, the wheat allergen status is `[INFERRED]` and therefore
becomes a gap, not a fact. Honor the hard-won distinctions: gelatin is its own
token and is not a meat allergen; pork-free/halal is a restriction layer, not an
allergen; watch for the dessert-mistagged-with-meat class of error. This stage is
where most gap questions are born.

### Stage 04 — Gap register (`04_gap_register.md`)
Collect every `[UNKNOWN]` and every safety-relevant `[INFERRED]` into a numbered
list of questions for the operator. **Rank safety-first:** allergen- and
restriction-affecting questions at the top, then ingredient identity, then
narrative/cultural gaps. Each question states the dish, the specific unknown, why it
matters, and (where helpful) a concrete multiple-choice framing that's easy for a
busy operator to answer ("Is the tempura fried in: a) pure vegetable oil, b) a blend
containing sesame oil, c) other?"). Good gap questions are the difference between a
B-grade record and an S-grade one.

### Stage 05 — Operator dialogue (`05_operator_dialogue.md`)
This is the clarification exchange. Run it two ways, and record both here:

- **Live:** when you're running interactively, ask the user (who stands in for the
  operator) the highest-priority safety questions directly in the conversation.
  Batch them sensibly — a handful at a time, safety questions first — rather than
  dumping the whole register. Take their answers as `[OPERATOR]`.
- **Async register:** `04_gap_register.md` itself is the artifact an operator can
  answer later. As answers come in, log them here with date and who answered.

Never let a "varies by item" answer cascade to individual dishes — if an operator
says frying oil "depends on the dish," that does not resolve the oil question for
any specific dish; keep those gaps open per-dish. Only record an answer as
`[OPERATOR]` when it actually pins down the specific field.

### Stage 06 — NFG output draft + verification gate (`06_nfg_output.md`)
Assemble the dataset in the shape of the NFG model: per dish, the Machine Semantics
half (ingredient_ids, method_ids, derived allergens, restrictions, taste profile,
calorie range) and the Human Narrative half (story, cultural context, serving
notes). Fold in the Stage 05 answers, upgrading provenance where the operator
confirmed things, and assign a provisional **`verification_rank`** per dish:

- **S** — every safety-relevant field is `[OPERATOR]` or `[CANONICAL]`; complete.
- **A** — core fields confirmed; only minor narrative gaps remain.
- **B** — significant fields still `[INFERRED]`, or open safety gaps remain.
- **C** — largely `[INFERRED]`; pre-operator-review draft.

End the file with the **verification gate** checklist (it's in the templates). The
record does not "pass" unless: no safety field rests on `[INFERRED]`/`[UNKNOWN]`;
every allergen traces to an ingredient; canonical overrides were applied; narrative
is separated from machine fields; and remaining incompleteness is stated explicitly
with its rank. A record that can't pass at S/A is fine — it ships at B/C *with the
gaps named*. Honest incompleteness beats fake completeness.

This is a **draft** until Stage 07. Mark the file header `status: draft (pending
operator sign-off)`. After sign-off, come back and finalize it: apply the operator's
corrections, upgrade confirmed fields to `[OPERATOR]`, recompute ranks, and change
the header to `status: finalized (operator-signed YYYY-MM-DD)`.

### Stage 07 — Operator review & sign-off (`07_operator_review.md`)
This is the second operator touchpoint and the moment VAD is actually earned. A
restaurant operator can only confirm what they can read and understand, so present
the *complete* assembled picture back to them in plain language — **in the
operator's own language** (for these Japanese restaurants, write the sheet in
Japanese; keep an English mirror only if the user asks). The point is to give them a
real chance to exercise judgment, especially over everything we could only infer.

Structure the sheet so it's easy for a busy owner to act on:

- **What we believe about each dish**, in plain terms — ingredients, how it's cooked,
  which allergens it carries, who can and can't eat it.
- **Flag every `[INFERRED]` item explicitly** as "我々の推測 — 要確認" (our
  assumption — please confirm). These are the lines the operator most needs to see:
  an `[INFERRED·high]` is still a guess, and the owner is the only one who can turn
  it into truth. Give each a dead-simple action: ✔ そのとおり (correct) / ✖ 違う →
  正しくは… (wrong → the right answer is…).
- **Show what's already solid** (`[MENU]`, `[CANONICAL]`, `[OPERATOR]`) separately,
  so the operator isn't asked to re-confirm things that don't need it — respect
  their time.
- **List what's still unanswered** from the gap register that blocks safe allergen
  answers, and what the current `verification_rank` means in one sentence ("at this
  level the concierge will say 'please check with staff' for X").

When the operator responds, log their confirmations and corrections here (dated,
attributed) as `[OPERATOR]` provenance, then return to Stage 06 and finalize. An
operator who downgrades our guess ("no, the karaage uses potato starch, not wheat")
is the system working exactly as intended — their correction outranks everything.

Until this sign-off happens, the dataset is a draft and the run summary should say
so. The deliverable of a fully successful run is a *finalized, operator-signed*
Stage 06 with the open-safety-gap count at zero.

## Working style

- **Don't invent to fill a template.** A blank tagged `[UNKNOWN]` is a successful
  output, not a failure. The gap register is where the value is.
- **Show the derivation, don't assert the conclusion.** For anything safety-related,
  the reader should be able to trace allergen → ingredient → source.
- **Prefer code over eyeballing for cross-checks.** If you need to confirm that
  every allergen in Stage 06 appears in Stage 03's derivation, or that no dish
  carries an allergen with `[INFERRED]` provenance, a short script is more reliable
  than rereading.
- **Treat `data_source` with care.** This protocol is for `live` restaurants. Never
  run write operations against corpus (`user_id = 19`) data.

When you finish a run, summarize for the user: how many dishes, how many reached
S/A, and the count of open safety gaps still blocking — that last number is the one
that matters most.
