from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm as ChangeForm
from django.contrib.auth.forms import UserCreationForm as CreationForm

from .models import User


class UserCreationForm(CreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserChangeForm(ChangeForm):
    class Meta:
        model = User
        fields = ["username", "display_username", "email", "password"]
