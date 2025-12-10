from django.tasks import task


@task
def upload(file_pk, temp_path, original_name, content_type):
    from django.core.files.storage import default_storage

    from .models import File

    file = File.objects.get(id=file_pk)
    key = f"users/{file.owner.pk}/files/{file_pk}"
    with open(temp_path, "rb") as f:
        default_storage.save(key, f)

    file.key = key
    file.name = original_name
    file.content_type = content_type
    file.size = default_storage.size(key)
    file.save()
