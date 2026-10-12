"""Phase 1, Step 1: project setup smoke tests."""

import pytest
from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import connection

from config.base_models import TimeStampedModel

LOCAL_APPS = [
    "core",
    "accounts",
    "vendors",
    "catalog",
    "bookings",
    "promotions",
    "cart",
    "orders",
    "payments",
    "reviews",
    "support",
    "storefront",
    "vendor_portal",
    "analytics",
]


@pytest.mark.parametrize("app_label", LOCAL_APPS)
def test_local_app_is_installed(app_label):
    assert apps.is_installed(app_label)


def test_database_is_postgresql():
    assert connection.vendor == "postgresql"


def test_localization_defaults():
    # NFR-04: English, PKR, Asia/Karachi; datetimes stored in UTC.
    assert settings.LANGUAGE_CODE == "en"
    assert settings.TIME_ZONE == "Asia/Karachi"
    assert settings.USE_TZ is True
    assert settings.CURRENCY_CODE == "PKR"


def test_custom_user_model_with_timestamps():
    # Rule 6 / NFR-09: every table has created_at and updated_at.
    user_model = get_user_model()
    assert user_model._meta.label == "accounts.User"
    assert issubclass(user_model, TimeStampedModel)


@pytest.mark.django_db
def test_user_timestamps_populate():
    user = get_user_model().objects.create_user(username="ali", password="x-StrongPass-123")
    assert user.created_at is not None
    assert user.updated_at is not None


def test_secret_key_comes_from_environment():
    # Rule 7: no hardcoded secret; settings require DJANGO_SECRET_KEY.
    assert settings.SECRET_KEY
    assert "insecure" not in settings.SECRET_KEY


@pytest.mark.django_db
def test_health_endpoint_reports_database_ok(client):
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": True}
