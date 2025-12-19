from pathlib import Path

from contrib.validators import FileUpload


def test_file_upload_call_preserves_extension():
    uploader = FileUpload(base_path="documents")
    result = uploader(None, "rel.PDF")
    assert result.startswith("documents/")
    assert result.endswith(".pdf")
    filename_part = Path(result).name
    assert len(filename_part) > 16


def test_file_upload_call_without_extension():
    uploader = FileUpload(base_path="backups")
    result = uploader(None, "README")
    assert "." not in Path(result).name
    assert result.startswith("backups/")


def test_file_upload_randomization():
    uploader = FileUpload(base_path="img")
    name = "photo.jpg"
    res1 = uploader(None, name)
    res2 = uploader(None, name)
    assert res1 != res2
    assert res1.endswith(".jpg")
    assert res2.endswith(".jpg")


def test_file_upload_base_path_strip():
    uploader = FileUpload(base_path="uploads///")
    result = uploader(None, "test.png")
    assert result.startswith("uploads/")
    assert not result.startswith("uploads//")
