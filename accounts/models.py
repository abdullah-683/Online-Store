from django.contrib.auth.models import AbstractUser

from config.base_models import TimeStampedModel


class User(TimeStampedModel, AbstractUser):
    """
    Single user table for customers, vendor team members and platform staff.

    Defined before the first migration so the custom user model can be
    extended later (phone, OTP verification, 2FA) without a painful swap.
    Vendor roles live on vendors.VendorMember, not here (FR-ROLE-01).
    """

    class Meta:
        db_table = "accounts_user"
