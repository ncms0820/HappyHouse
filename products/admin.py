from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category Admin Definition"""

    pass


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
        "category",
    )

    list_filter = ("seller",)
