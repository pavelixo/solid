import pytest
from authentication.models import User

@pytest.mark.django_db
class TestUserManager:

    def test_create_user_success(self):
        email = " test@EXAMPLE.COM "
        username = " TestUser "
        user = User.objects.create_user(username=username, email=email, password="password123")

        assert user.email == "test@example.com"
        assert user.username == "testuser"
        assert user.display_username == "testuser"
        assert user.is_staff is False
        assert user.is_superuser is False
        assert user.check_password("password123")

    def test_create_superuser_success(self):
        user = User.objects.create_superuser(
            username="admin", email="admin@test.com", password="password123"
        )

        assert user.is_staff is True
        assert user.is_superuser is True

    def test_create_user_missing_username(self):
        with pytest.raises(ValueError, match="Username field must be set"):
            User.objects.create_user(username="", email="test@test.com")

    def test_create_user_missing_email(self):
        with pytest.raises(ValueError, match="Email field must be set"):
            User.objects.create_user(username="test", email="")

    def test_create_superuser_invalid_flags(self):
        with pytest.raises(ValueError, match="Superuser must have is_staff=True."):
            User.objects.create_superuser(
                username="admin", email="a@a.com", password="123", is_staff=False
            )

        with pytest.raises(ValueError, match="Superuser must have is_superuser=True."):
            User.objects.create_superuser(
                username="admin2", email="b@b.com", password="123", is_superuser=False
            )