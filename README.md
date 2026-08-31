# SummerSuite — Matching Engine

Backend matching logic for **SummerSuite**, a roommate-matching platform for interns and new grads relocating to a new city for work. This repo contains the matching engine specifically — the piece of the larger team project I designed and built.

## What it does

Given a user and a list of candidate roommates, the engine:

1. **Filters** candidates through a set of hard constraints (must all pass to be considered eligible)
2. **Scores** the remaining eligible candidates on softer, weighted preferences
3. **Ranks** candidates by match score, highest first

## Architecture

- `matching/base.py` / `matching/scoring_base.py` — abstract base classes (`HardFilter`, `ScoringFactor`) that define the interface every filter/factor implements
- `matching/filters.py` — hard filters: budget overlap, age range, gender preference, move-in date tolerance, smoking, pet allergies, and location range (via haversine distance)
- `matching/factors.py` — weighted scoring factors: cleanliness, sleep schedule, temperature preference, lease duration, cooking habits, room occupancy, and interest overlap (Jaccard similarity)
- `matching/registry.py` / `matching/scoring_registry.py` — central registries listing which filters/factors are active, so new ones can be added without touching the engine itself
- `matching/eligibility.py` — runs a candidate through all active hard filters
- `matching/engine.py` — computes a weighted match score (0–1) across all active scoring factors, skipping unanswered fields rather than penalizing them
- `matching/pipeline.py` — ties it together: filters candidates, scores the eligible ones, returns them ranked

## Design notes

- Filters and scoring factors are separate, single-responsibility classes rather than one large conditional block — new criteria can be added by writing one class and registering it.
- Missing/unanswered user fields are treated as "skip this factor," not as a mismatch — a user who hasn't filled out every field yet isn't penalized for it.
- Hard filters are pass/fail (eligibility); scoring factors are weighted and continuous (ranking).

## Status

The filter and scoring logic here is complete for the v1 matching pipeline. Verification scripts are included under `matching/test_*.py` covering the filters, factors, eligibility check, engine scoring, and the full ranking pipeline — these currently print actual vs. expected output for manual verification rather than using an assertion-based test framework; converting them to `pytest` is a near-term next step.

This is the backend for a larger full-stack project — a teammate is building the React/TypeScript frontend and we're integrating against a shared Supabase database.
