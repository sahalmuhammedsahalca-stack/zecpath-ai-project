from datetime import datetime, timedelta, timezone
from pathlib import Path


class DataRetentionPolicy:
    """
    Defines retention periods for Zecpath AI data.

    Default retention periods:
    - Audit logs: 365 days
    - Transcripts: 180 days
    - Reports: 365 days
    """

    DEFAULT_RETENTION_DAYS = {
        "audit_logs": 365,
        "transcripts": 180,
        "reports": 365,
    }

    def __init__(self, retention_days=None):
        self.retention_days = (
            retention_days
            if retention_days is not None
            else self.DEFAULT_RETENTION_DAYS.copy()
        )

    def get_retention_days(self, data_type: str) -> int:
        if data_type not in self.retention_days:
            raise ValueError(f"Unsupported data type: {data_type}")

        return self.retention_days[data_type]

    def calculate_expiry(self, created_at: datetime, data_type: str) -> datetime:
        retention_days = self.get_retention_days(data_type)

        return created_at + timedelta(days=retention_days)

    def is_expired(self, created_at: datetime, data_type: str) -> bool:
        expiry_date = self.calculate_expiry(created_at, data_type)

        return datetime.now(timezone.utc) >= expiry_date

    def should_delete_file(
        self,
        file_path: str,
        data_type: str,
    ) -> bool:
        path = Path(file_path)

        if not path.exists():
            return False

        created_at = datetime.fromtimestamp(
            path.stat().st_mtime,
            tz=timezone.utc,
        )

        return self.is_expired(created_at, data_type)