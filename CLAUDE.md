# Project: Multi-Vendor Marketplace (Pakistan)

## Context
Multi-vendor marketplace where independent vendors sell products and services. The
approved requirements are in docs/REQUIREMENTS.md — the source of truth. Reference
requirement IDs (FR-CAT-01, SEC-05, etc.) in code comments, commits and tests.

## Tech stack (decided; do not change without asking)
- Python 3.12+, Django 5.2 LTS, PostgreSQL
- Django templates + Tailwind CSS + htmx
- Celery + Redis for background jobs
- S3-compatible storage for media
- Analytics: GA4, BigQuery, Looker Studio

## Core design rules
1. Every listing is a Product or Service (one Listing model with a type field).
2. Vendors define their own option types and values per listing; each option
   combination is a Variant with its own SKU, optional price override and stock.
3. One customer Order splits into one VendorOrder per vendor; OrderItems store
   snapshots (name, options, SKU, price paid, customer instructions).
4. Commission is calculated on the discounted price actually paid; shipping
   passes through to the vendor.
5. Vendor data isolation is mandatory: every vendor-portal query is filtered by
   the current user's vendor. Never use unfiltered querysets in vendor views.
6. Every table has created_at and updated_at timestamps — inherit
   `config.base_models.TimeStampedModel`.
7. Secrets live in .env and are never committed.

## How to work
- Build in small, testable steps following the roadmap phases and "Done when" criteria.
  Finish and verify one step before starting the next.
- At each step: explain what is being built, build it, then give exact test steps.
- Ask before making any decision not covered by the requirements document.
- Write automated tests for checkout, order splitting, commission and permissions.

## Commands
- Tests: `pytest` (settings: `config.settings.test`, tests live in `tests/`)
- Lint/format: `ruff check . && ruff format --check .`
- Migrations check: `python manage.py makemigrations --check --dry-run`
