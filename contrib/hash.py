from django.utils.crypto import get_random_string
from django.utils.deconstruct import deconstructible


@deconstructible
class RandomHash:
    LENGTH = 12
    ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789"

    def __init__(self, length=None, allowed_chars=None):
        self.length = length or self.LENGTH
        self.allowed_chars = allowed_chars or self.ALLOWED_CHARS

    def __call__(self):
        return get_random_string(self.length, self.allowed_chars)
