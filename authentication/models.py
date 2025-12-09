from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import AbstractUser, AbstractUserManager


class UserManager(AbstractUserManager):
    """
    Custom user manager that extends the AbstractUserManager
    to handle user creation and superuser creation with additional
    validation and normalization.
    """

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        This method normalizes the email and username before creating the user.
        """

        if not username:
            raise ValueError(_("Username field must be set"))

        if not email:
            raise ValueError(_("Email field must be set"))

        email = self.normalize_email(email)
        username = self.normalize_username(username)

        user = self.model(
            username=username, display_username=username, email=email, **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Create a regular user with the given username, email, and password.
        This method sets default values for is_staff and is_superuser.
        """

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Create a superuser with the given username, email, and password.
        This method sets default values for is_staff and is_superuser and
        ensures that these values are True.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


