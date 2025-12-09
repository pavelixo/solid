import re
from pathlib import Path
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

    def __init__(self, base_path="uploads"):
        """
        base_path: directory where files will be stored.
        Example: 'avatars/', 'posts/images/', etc.
        """
        self.base_path = base_path.rstrip("/")

    def __call__(self, instance, filename):
        """
        Generates a random filename while preserving the file extension.
        Combines the configured path with the generated filename.
        """

        match = self.EXT_REGEX.search(filename)
        ext = match.group(1).lower() if match else ""
        mark = token_urlsafe(16).lower()
        new_filename = f"{mark}.{ext}" if ext else mark

        return str(Path(self.base_path) / new_filename)
