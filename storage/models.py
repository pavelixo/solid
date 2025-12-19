from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User
from contrib.hash import RandomHash


class Folder(models.Model):
    random_hash = RandomHash()
    id = models.CharField(
        primary_key=True,
        max_length=32,
        default=random_hash,
        editable=False,
    )
    name = models.CharField(_("name"), max_length=255)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="subfolders",
        verbose_name=_("subfolder"),
        on_delete=models.CASCADE,
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("owner"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    is_deleted = models.BooleanField(_("is deleted"), default=False)
    deleted_at = models.DateTimeField(_("deleted at"), null=True, blank=True)

    class Meta:
        verbose_name = _("folder")
        verbose_name_plural = _("folders")

    def __str__(self):
        return self.name


class File(models.Model):
    random_hash = RandomHash()
    id = models.CharField(
        primary_key=True,
        max_length=32,
        default=random_hash,
        editable=False,
    )

    folder = models.ForeignKey(
        Folder,
        related_name="files",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("folder"),
    )

    name = models.CharField(_("name"), max_length=255)
    key = models.CharField(_("key"), max_length=512)
    size = models.BigIntegerField(_("size"))
    content_type = models.CharField(_("content type"), max_length=100)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("owner"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    is_deleted = models.BooleanField(_("is deleted"), default=False)
    deleted_at = models.DateTimeField(_("deleted at"), null=True, blank=True)

    class Meta:
        verbose_name = _("file")
        verbose_name_plural = _("files")

    def __str__(self):
        return self.name
