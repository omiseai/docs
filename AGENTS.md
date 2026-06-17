> **First-time setup**: Customize this file for your project. Prompt the user to customize this file for their project.
> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Documentation project instructions

## About this project

- This is a documentation site built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- Run `mint dev` to preview locally
- Run `mint broken-links` to check links

## Terminology

{/* Add product-specific terms and preferred usage */}
{/* Example: Use "workspace" not "project", "member" not "user" */}

## Style preferences

{/* Add any project-specific style rules below */}

- Use active voice and second person ("you")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references

## Content boundaries

{/* Define what should and shouldn't be documented */}
{/* Example: Don't document internal admin features */}

# CLAUDE.md — NGraph / OMISEAI

## What this project is

**OMISEAI** (customer brand) / **NGraph** (platform) is a per-restaurant AI concierge SaaS built in Japan. Diners scan a QR code and chat with an AI that knows the restaurant's menu in depth — ingredients, allergens, cultural context, drink pairings — in 28 languages. Restaurants pay a monthly subscription.

The long-game product is **NFG (Nicomacos Food Graph)**: a verified, structured data standard for what a dish *means*. The thesis: AI agents will mediate how people choose restaurants; NFG aims to be the authoritative, owner-verified data layer those agents reference ("JAN code of food"). External API planned for AI agents and booking services.

Key concept: **VAD (Verified Authentic Data)** — AI structures ~90%, the owner confirms. Verified data always outranks AI-generated guesses (`verification_rank`).

## Architecture

```
Diner (QR) → app.ngraph.jp (Next.js, nginx on EC2)
           → dev-backend.ngraph.jp (nginx reverse proxy)
           → FastAPI (Docker Compose, EC2 t3.small)
               ├── chat agent (gpt-4o-mini + function tools)
               ├── camera menu analysis (Vision)
               ├── admin API (menus, NFG editor, analytics)
               ├── celery-worker / celery-beat
               └── redis (cache + task queue)
           → PostgreSQL 17 (RDS ap-northeast-1)
```

## Core design principles

- **Speed over prompt size**: system prompt stays small; details fetched on demand via function tools. `max_completion_tokens=2048`. Diner-facing → gpt-4o-mini; admin/one-shot → gpt-4o.
- **Generate once, serve from DB**: NFG enrichment (narrative, descriptions, serving notes) generated once by gpt-4o via scripts and stored. Chat reads the DB — never re-generates on request.
- **Ground everything**: drink queries go through `list_drinks` (DB-grounded); camera matching requires ≥0.85 confidence + category match or falls back gracefully. LLM free-generation about store data is a bug.
- **HITL / VAD**: owner-confirmed data outranks AI guesses at all times.

## Live data vs. corpus data — CRITICAL

- **Live restaurants** (`data_source = 'live'`): 10 real paying customers (Bonta Group x6, Giorno x2, Acoya, RAMEN W). All write operations (allergen backfill, enrichment, question gen, etc.) must target only these.
- **Corpus data**: ~1,300 restaurants / 27k menus imported from Google API for training vocabulary. These belong to `user_id = 19`. **Never run write operations against corpus data.**

## Key data assets

| Asset | Description |
|---|---|
| `product_master.json` | 244 verified drink/ingredient canonical entries (sake breweries' official specs). Overrides GPT guesses → no hallucination. |
| `ingredient_glossary.json` | 481 ingredient terms with verified English canonical names. |
| Food-culture knowledge base | 99 verified regional dishes (MAFF "Our Regional Cuisines" source). |

Allergen schema: 32 items, 5-country mapping.

## Pricing

| Plan | Price |
|---|---|
| Light | ¥3,980 / month |
| Base | ¥9,800 / month |
| Enterprise | ¥19,800 / month |

LP currently runs ¥1,980 early-bird lead campaign (marketing only, not the real price card).

## Key docs (in repo)

- `ngraph/docs/SYSTEM_SPEC.md` — master spec: data model, API, business rules, prohibited changes
- `ngraph/docs/PLAN.md` / `ngraph/docs/HANDOVER.md` — current plan / last-session handover
- `ngraph/docs/OMISEAI_BUSINESS_PLAN.md` — business plan master (~800 lines)
- `ngraph/docs/NFG_data_master.md`, `ngraph/docs/NFG_philosophy.md` — NFG data model & design philosophy

## Near-term context

- JSSA Osaka pitch: 2026-06-29
- First VC meeting (Genesia Ventures) being scheduled
- Matt's first focus area: unit economics, then external-AI-reference story for NFG

## Validation commands

_Add project-specific lint / test / type-check commands here once confirmed._
