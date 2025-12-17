from django.core.files.storage import default_storage
from django.tasks import task

from .models import File


@task
def upload(file_pk, temp_path, original_name, content_type):
    # Validate inputs
    if not file_pk or not temp_path or not original_name or not content_type:
        raise ValueError("Missing required parameters")
    
    try:
        file = File.objects.get(id=file_pk)
    except File.DoesNotExist:
        raise ValueError(f"File with id {file_pk} not found")
    
    # Validate file exists and is readable
    try:
        with open(temp_path, "rb") as f:
            key = f"users/{file.owner.pk}/files/{file_pk}"
            default_storage.save(key, f)
    except FileNotFoundError:
        raise ValueError(f"Temporary file not found: {temp_path}")
    except IOError as e:
        raise ValueError(f"Failed to read file: {str(e)}")
    
    file.key = key
    file.name = original_name
    file.content_type = content_type
    file.size = default_storage.size(key)
    file.save()
