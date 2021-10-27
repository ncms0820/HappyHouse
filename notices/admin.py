from django.contrib import admin
from . import models


@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):

    """Notice Admin Definition"""

    list_display = (
        "title",
        "writer",
    )
    list_filter = ("writer",)
