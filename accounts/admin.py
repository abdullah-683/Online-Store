from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class MarketplaceUserAdmin(UserAdmin):
    readonly_fields = ("created_at", "updated_at", "last_login", "date_joined")
