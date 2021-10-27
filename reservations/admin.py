from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Admin"""

    list_display = (
        "__str__",
        "check_in",
        "check_out",
        "status",
        "is_progress",
        "is_finished",
    )

    list_filter = ("status",)
