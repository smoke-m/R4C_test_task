from django.conf import settings
from django.contrib import admin

from .models import Robot, RobotModel


@admin.register(RobotModel)
class RobotModelAdmin(admin.ModelAdmin):
    """Админ зона Order."""

    list_display = ("model_ind",)
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ("model_ind",)


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    """Админ зона Order."""

    list_display = (
        "serial",
        "model",
        "version",
        "created",
    )
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ("serial",)
