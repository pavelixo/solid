from secrets import token_urlsafe

from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User


def hash():
    return token_urlsafe(12)


class Folder(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=hash, editable=False)
    name = models.CharField(_("name"), max_length=255)
    parent = models.ForeignKey(
        _("parent"),
        "self",
        null=True,
        blank=True,
        related_name="subfolders",
        on_delete=models.CASCADE,
    )

    owner = models.ForeignKey(_("owner"), User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        verbose_name = _("folder")
        verbose_name_plural = _("folders")
        abstract = True


class File(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=hash, editable=False)

    folder = models.ForeignKey(
        _("folder"),
        Folder,
        related_name="files",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    name = models.CharField(_("name"), max_length=255)
    key = models.CharField(_("key"), max_length=512)
    size = models.BigIntegerField(_("size"))
    content_type = models.CharField(_("content type"), max_length=100)

    owner = models.ForeignKey(_("owner"), User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
