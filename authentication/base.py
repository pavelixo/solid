from functools import reduce

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from contrib.validators import UsernameValidator


class AbstractUserManager(BaseUserManager):
    @classmethod
    def normalize_username(cls, username):
        """
        Normalize the given username by applying a series of transformations:
        stripping whitespace and converting to lowercase.

        Args:
            username (str): The username to be normalized.

        Returns:
            str: The normalized username after applying all transformations.
        """

        normalization_functions = [
            lambda string: string.strip(),
            lambda string: string.lower(),
        ]

        normalized_username = reduce(
            lambda acc, func: func(acc), normalization_functions, username
        )

        return normalized_username


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    Abstract base class for user models, providing core fields and methods.
    This class is designed to be extended by concrete user models, offering
    a foundation for user authentication and management.
    """

    username_validator = UsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=32,
        unique=True,
        help_text=_(
            "Required. 32 characters or fewer." "Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists.")},
    )

    email = models.EmailField(_("email address"), unique=True, blank=False)

    is_staff = models.BooleanField(
        _("is staff"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("is active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
