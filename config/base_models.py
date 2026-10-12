"""Shared abstract base models used by every app."""

from django.db import models


class TimeStampedModel(models.Model):
    """
    Adds created_at / updated_at to every table.

    Required on all tables for incremental ETL to BigQuery (NFR-09).
    """

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
