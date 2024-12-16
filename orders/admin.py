from django.conf import settings
from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админ зона Order."""

    list_display = (
        "customer",
        "robot_serial",
        "completed",
    )
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ("customer",)
