from django.contrib import admin

from .models import File, Folder


class FolderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "parent",
        "created_at",
        "updated_at",
        "is_deleted",
    )

    list_filter = (
        "owner",
        "is_deleted",
        "created_at",
    )

    search_fields = (
        "name",
        "id",
        "owner__username",
        "parent__name",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
        "deleted_at",
    )

    fieldsets = (
        (
            "Folder Information",
            {
                "fields": (
                    "id",
                    "name",
                    "parent",
                )
            },
        ),
        (
            "Ownership",
            {"fields": ("owner",)},
        ),
        (
            "Status",
            {
                "fields": (
                    "is_deleted",
                    "deleted_at",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


class FileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "folder",
        "size",
        "content_type",
        "created_at",
        "is_deleted",
    )

    list_filter = (
        "owner",
        "content_type",
        "is_deleted",
        "created_at",
    )

    search_fields = (
        "name",
        "id",
        "key",
        "owner__username",
        "folder__name",
    )

    readonly_fields = (
        "id",
        "key",
        "size",
        "created_at",
        "updated_at",
        "deleted_at",
    )

    fieldsets = (
        (
            "File Info",
            {
                "fields": (
                    "id",
                    "name",
                    "folder",
                    "content_type",
                )
            },
        ),
        (
            "Storage Metadata",
            {
                "fields": (
                    "key",
                    "size",
                )
            },
        ),
        (
            "Ownership",
            {"fields": ("owner",)},
        ),
        (
            "Status",
            {
                "fields": (
                    "is_deleted",
                    "deleted_at",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


admin.site.register(Folder, FolderAdmin)
admin.site.register(File, FileAdmin)
