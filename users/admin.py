from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "manager",
        "is_staff",
        "apartment",
    )
    list_filter = UserAdmin.list_filter + ("manager", "apartment")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "apartment",
                    "manager",
                    "cart",
                )
            },
        ),
    )
    filter_horizontal = ("cart",)
