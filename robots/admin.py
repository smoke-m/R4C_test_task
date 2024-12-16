from django.conf import settings
from django.contrib import admin

from .models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    """Админ зона Order."""

    list_display = (
        'serial',
        'model',
        'version',
        'created',
    )
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ('serial',)
