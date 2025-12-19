import pytest

from authentication.models import User
from storage.models import File, Folder


@pytest.mark.django_db
class TestModelStr:

    @pytest.fixture
    def user(self):
        return User.objects.create_user(username="owner", email="owner@test.com")

    def test_folder_str(self, user):
        folder = Folder.objects.create(name="My Folder", owner=user)
        assert str(folder) == "My Folder"

    def test_file_str(self, user):
        folder = Folder.objects.create(name="Photos", owner=user)

        file = File.objects.create(
            name="vacation.jpg",
            folder=folder,
            owner=user,
            key="path/to/vacation.jpg",
            size=1024,
            content_type="image/jpeg",
        )

        assert str(file) == "vacation.jpg"
