import re
from secrets import token_urlsafe

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


@deconstructible
class FileUpload:
    EXT_REGEX = re.compile(r"\.([A-Za-z0-9]+)$")

    def __call__(self, instance, filename):
        """
        Generates the new filename using a random string and file extension.
        """

        match = self.EXT_REGEX.search(filename)
        ext = match.group(1) if match else ""

        mark = token_urlsafe(16).lower()
        return f"{mark}.{ext}" if ext else mark
