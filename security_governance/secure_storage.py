from pathlib import Path


class SecureStorageManager:
    """
    Defines controlled storage locations for sensitive Zecpath AI data.
    """

    STORAGE_TYPES = {
        "transcripts": "secure_storage/transcripts",
        "reports": "secure_storage/reports",
    }

    def __init__(self, base_directory: str = "security_governance"):
        self.base_directory = Path(base_directory)

    def get_storage_path(self, data_type: str) -> Path:
        if data_type not in self.STORAGE_TYPES:
            raise ValueError(f"Unsupported storage type: {data_type}")

        path = self.base_directory / self.STORAGE_TYPES[data_type]

        path.mkdir(parents=True, exist_ok=True)

        return path

    def validate_filename(self, filename: str) -> bool:
        path = Path(filename)

        if path.name != filename:
            return False

        if ".." in path.parts:
            return False

        return True

    def get_file_path(
        self,
        data_type: str,
        filename: str,
    ) -> Path:
        if not self.validate_filename(filename):
            raise ValueError("Invalid filename")

        return self.get_storage_path(data_type) / filename