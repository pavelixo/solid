from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ("username", "display_username", "email", "is_staff", "is_superuser")

    fieldsets = (
        (
            None,
            {"fields": ("avatar", "username", "display_username", "email", "password")},
        ),
        ("Permissions", {"fields": ("is_superuser", "is_staff")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, UserAdmin)
