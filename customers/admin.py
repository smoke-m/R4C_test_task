from django.conf import settings
from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Админ зона Customer."""

    list_display = (
        'email',
    )
    empty_value_display = settings.EMPTY_VALUE
    list_filter = ('email',)
