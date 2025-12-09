from secrets import token_urlsafe

from django.db import models

from authentication.models import User


def hash():
    return token_urlsafe(12)


class Folder(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=hash, editable=False)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="subfolders",
        on_delete=models.CASCADE,
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class File(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=hash, editable=False)

    folder = models.ForeignKey(
        Folder, related_name="files", null=True, blank=True, on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)
    key = models.CharField(max_length=512)
    size = models.BigIntegerField()
    content_type = models.CharField(max_length=100)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
