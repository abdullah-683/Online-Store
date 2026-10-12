# Multi-Vendor Marketplace (Pakistan)

Independent vendors sell products and services; the platform collects payments and
earns a commission. Requirements and roadmap: [`docs/REQUIREMENTS.md`](docs/REQUIREMENTS.md)
(source of truth).

**Stack:** Python 3.12+, Django 5.2 LTS, PostgreSQL, Django templates + Tailwind CSS +
htmx, Celery + Redis, S3-compatible media storage.

## Local setup

Prerequisites: Python 3.12+, PostgreSQL 14+, Redis (only needed once Celery tasks exist).

```bash
# 1. Clone and create a virtual environment
git clone https://github.com/abdullah-683/Online-Store.git
cd Online-Store
python3.12 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

# 2. Create the PostgreSQL role and database
#    (CREATEDB lets the test runner create its throwaway test database)
sudo -u postgres psql -c "CREATE ROLE marketplace LOGIN PASSWORD 'marketplace' CREATEDB;"
sudo -u postgres createdb -O marketplace marketplace

# 3. Configure environment variables
cp .env.example .env
python -c "import secrets; print(secrets.token_urlsafe(50))"   # paste into DJANGO_SECRET_KEY

# 4. Migrate, create an admin user, run
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Health check: http://127.0.0.1:8000/health/ → `{"status": "ok", "database": true}`
- Admin panel: http://127.0.0.1:8000/admin/ (path configurable via `DJANGO_ADMIN_URL`)

## Settings

`config/settings/` is split by environment; all secrets come from environment variables
(`.env` locally, never committed).

| Module | Used by | Notes |
|---|---|---|
| `base.py` | all | Apps, DB, auth, i18n (Asia/Karachi, PKR), storage, Celery |
| `dev.py` | `manage.py` (default) | `DEBUG=True` |
| `test.py` | pytest | Fast hashing, eager Celery, in-memory storage |
| `prod.py` | `wsgi.py` / `asgi.py` | HTTPS, HSTS, secure cookies (SEC-14) |

## Quality checks

```bash
pytest                      # automated tests (tests/)
ruff check . && ruff format --check .
python manage.py makemigrations --check --dry-run
```

## Project layout

One Django project, one app per business area: `core`, `accounts`, `vendors`, `catalog`,
`bookings`, `promotions`, `cart`, `orders`, `payments`, `reviews`, `support`,
`storefront`, `vendor_portal`, `analytics`. Shared abstract models (e.g.
`TimeStampedModel`) live in `config/base_models.py`.
