import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


class AuditLogger:
    """
    Handles audit trail records for Zecpath AI.

    Two audit event types are supported:
    - Score logs
    - Decision logs
    """

    def __init__(self, log_directory: str = "security_governance/audit_logs"):
        self.log_directory = Path(log_directory)
        self.log_directory.mkdir(parents=True, exist_ok=True)

        self.score_log_file = self.log_directory / "score_logs.jsonl"
        self.decision_log_file = self.log_directory / "decision_logs.jsonl"

    def _create_timestamp(self) -> str:
        """Return the current UTC timestamp."""
        return datetime.now(timezone.utc).isoformat()

    def _write_log(self, file_path: Path, record: Dict[str, Any]) -> Dict[str, Any]:
        """Append one audit record to a JSON Lines file."""
        with file_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")

        return record

    def log_score(
        self,
        candidate_id: str,
        round_name: str,
        score: float,
        scoring_source: str,
    ) -> Dict[str, Any]:
        """
        Record a candidate scoring event.
        """
        record = {
            "event_type": "score",
            "timestamp": self._create_timestamp(),
            "candidate_id": candidate_id,
            "round_name": round_name,
            "score": score,
            "scoring_source": scoring_source,
        }

        return self._write_log(self.score_log_file, record)

    def log_decision(
        self,
        candidate_id: str,
        decision: str,
        confidence: float,
        decision_source: str,
    ) -> Dict[str, Any]:
        """
        Record a candidate hiring decision.
        """
        record = {
            "event_type": "decision",
            "timestamp": self._create_timestamp(),
            "candidate_id": candidate_id,
            "decision": decision,
            "confidence": confidence,
            "decision_source": decision_source,
        }

        return self._write_log(self.decision_log_file, record)

    def read_logs(self, log_type: str) -> list[Dict[str, Any]]:
        """
        Read audit records from the requested log.

        Supported values:
        - score
        - decision
        """
        if log_type == "score":
            file_path = self.score_log_file
        elif log_type == "decision":
            file_path = self.decision_log_file
        else:
            raise ValueError("log_type must be 'score' or 'decision'")

        if not file_path.exists():
            return []

        records = []

        with file_path.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    records.append(json.loads(line))

        return records