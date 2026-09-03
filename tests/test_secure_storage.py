from security_governance.secure_storage import SecureStorageManager


def test_transcript_storage(tmp_path):
    manager = SecureStorageManager(str(tmp_path))

    path = manager.get_storage_path("transcripts")

    assert path.exists()
    assert path.is_dir()


def test_report_storage(tmp_path):
    manager = SecureStorageManager(str(tmp_path))

    path = manager.get_storage_path("reports")

    assert path.exists()
    assert path.is_dir()


def test_file_path(tmp_path):
    manager = SecureStorageManager(str(tmp_path))

    path = manager.get_file_path(
        "reports",
        "candidate_report.json",
    )

    assert path.name == "candidate_report.json"


def test_invalid_filename(tmp_path):
    manager = SecureStorageManager(str(tmp_path))

    try:
        manager.get_file_path(
            "reports",
            "../secret.txt",
        )
        assert False
    except ValueError:
        assert True