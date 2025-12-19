from django.core.files.storage import default_storage
from django_tasks import task

from .models import File


@task
def upload(file_pk, temp_path, original_name, content_type):
    if not all([file_pk, temp_path, original_name, content_type]):
        raise ValueError("Missing required parameters")

    try:
        file = File.objects.get(pk=file_pk)
    except File.DoesNotExist:
        raise ValueError(f"File with id {file_pk} not found")

    key = f"users/{file.owner.pk}/files/{file_pk}"
    try:
        with open(temp_path, "rb") as f:
            default_storage.save(key, f)
    except FileNotFoundError:
        raise ValueError(f"Temporary file not found: {temp_path}")
    except IOError as e:
        raise ValueError(f"Failed to read file: {str(e)}")

    file.key = key
    file.name = original_name
    file.content_type = content_type
    try:
        file.size = default_storage.size(key)
    except Exception as e:
        raise ValueError(f"Failed to get file size: {str(e)}")

    file.save()
