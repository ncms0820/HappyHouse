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


@admin.register(models.Comments)
class CommentAdmin(admin.ModelAdmin):

    """Comments Admin Definition"""

    pass
