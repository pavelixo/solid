from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    """
    Validator for usernames.

    Ensures that the username contains only
    letters, numbers, and the following special characters:
    - . (dot)
    - _ (underscore)
    - - (hyphen)
    """

    regex = r"^[\w.-]+$"
    message = _(
        "Enter a valid username. "
        "This value may contain only "
        "letters, numbers, and the following special characters: "
        "- . (dot), _ (underscore), and - (hyphen)."
    )
    flags = 0
