from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = (
        "__str__",
        "product",
        "seller",
        "get_thumbnail",
    )

    list_filter = ("product",)

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.photo.url}"/>')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.Category)
class TypeAdmin(admin.ModelAdmin):

    """Type Admin Definition"""

    list_display = ("category",)

    filter_horizontal = ("product",)


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    """Product Admin Definition"""

    inlines = (PhotoInline,)

    list_display = (
        "name",
        "price",
        "description",
        "seller",
    )

    list_filter = ("seller",)
