import pytest
from unittest.mock import patch
from django.core.files.storage import default_storage
from authentication.models import User
from storage.models import File
from storage.tasks import upload


@pytest.mark.django_db
class TestUploadTask:

    @pytest.fixture
    def user(self):
        return User.objects.create_user(username="error_user", email="err@test.com")

    @pytest.fixture
    def file_instance(self, user):
        return File.objects.create(name="test.txt", owner=user, size=0)

    # --- Exception Tests ---

    def test_raise_missing_parameters(self):
        with pytest.raises(ValueError, match="Missing required parameters"):
            upload.func(None, "", "name.txt", "text/plain")

    def test_raise_file_does_not_exist(self):
        with pytest.raises(ValueError, match="File with id 999 not found"):
            upload.func(999, "/tmp/file.txt", "name.txt", "text/plain")

    def test_raise_file_not_found_os(self, file_instance):
        with pytest.raises(ValueError, match="Temporary file not found"):
            upload.func(file_instance.pk, "/tmp/non_existent_path_123.txt", "n.txt", "t/p")

    def test_raise_io_error_on_open(self, file_instance):
        # Translated "Permissão negada" to "Permission denied"
        with patch("builtins.open", side_effect=IOError("Permission denied")):
            with pytest.raises(ValueError, match="Failed to read file: Permission denied"):
                upload.func(file_instance.pk, "/tmp/fake.txt", "n.txt", "t/p")

    def test_raise_error_getting_storage_size(self, file_instance, tmp_path):
        temp_file = tmp_path / "valid.txt"
        temp_file.write_bytes(b"data")

        with patch("django.core.files.storage.default_storage.size") as mock_size:
            mock_size.side_effect = Exception("Storage connection timeout")
            
            with pytest.raises(ValueError, match="Failed to get file size: Storage connection timeout"):
                upload.func(file_instance.pk, str(temp_file), "test.txt", "text/plain")

    # --- Persistence Test (file.save) ---

    def test_upload_success_persistence(self, file_instance, tmp_path):
        """Tests if file.save() correctly persists data in the database."""
        # Preparation
        temp_file = tmp_path / "final_file.txt"
        content = b"hello world persistence"
        temp_file.write_bytes(content)
        
        new_name = "new_filename.txt"
        new_ctype = "text/plain"

        # Execution
        upload.func(
            file_pk=file_instance.pk,
            temp_path=str(temp_file),
            original_name=new_name,
            content_type=new_ctype
        )

        # Verification of file.save()
        file_instance.refresh_from_db() # Pulls the new data saved by the task
        
        assert file_instance.name == new_name
        assert file_instance.content_type == new_ctype
        assert file_instance.size == len(content)
        assert file_instance.key == f"users/{file_instance.owner.pk}/files/{file_instance.pk}"
        
        # Storage cleanup
        default_storage.delete(file_instance.key)