import pytest
from django.core import mail

from authentication.base import AbstractUserManager
from authentication.models import User


def test_normalize_username_basic():
    input_username = "  UserNAME  "
    expected = "username"

    assert AbstractUserManager.normalize_username(input_username) == expected


@pytest.mark.parametrize(
    "input_val, expected_output",
    [
        ("ALICE", "alice"),
        ("  bob  ", "bob"),
        ("\tCharlie\n", "charlie"),
        ("jane-doe", "jane-doe"),
    ],
)
def test_normalize_username_scenarios(input_val, expected_output):
    assert AbstractUserManager.normalize_username(input_val) == expected_output


@pytest.mark.django_db
def test_user_email_user_method_sends_email():
    user = User.objects.create_user(
        username="TestUser", email="test@example.com", password="password123"
    )

    subject = "Account Activation"
    message = "Click the link to activate your account."
    user.email_user(subject=subject, message=message)

    assert len(mail.outbox) == 1
    sent_email = mail.outbox[0]

    assert sent_email.subject == subject
    assert sent_email.body == message
    assert sent_email.to == [user.email]
    assert sent_email.from_email is not None


@pytest.mark.django_db
def test_user_email_user_with_custom_from_email():
    user = User.objects.create_user(username="admin_user", email="admin@example.com")

    custom_from = "no-reply@mysite.com"
    user.email_user("Subject", "Message", from_email=custom_from)

    assert mail.outbox[0].from_email == custom_from
