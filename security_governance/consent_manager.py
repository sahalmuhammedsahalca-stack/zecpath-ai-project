from datetime import datetime, timezone


class ConsentManager:
    """
    Manages candidate consent for AI data processing.
    """

    ALLOWED_PURPOSES = {
        "recruitment_evaluation",
        "interview_analysis",
        "report_generation",
        "audit",
    }

    def __init__(self):
        self._consents = {}

    def record_consent(
        self,
        candidate_id: str,
        purposes: list[str],
    ) -> dict:
        invalid_purposes = set(purposes) - self.ALLOWED_PURPOSES

        if invalid_purposes:
            raise ValueError(
                f"Unsupported consent purposes: {sorted(invalid_purposes)}"
            )

        record = {
            "candidate_id": candidate_id,
            "purposes": sorted(set(purposes)),
            "consent_given": True,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self._consents[candidate_id] = record

        return record

    def revoke_consent(self, candidate_id: str) -> bool:
        if candidate_id not in self._consents:
            return False

        self._consents[candidate_id]["consent_given"] = False
        self._consents[candidate_id]["revoked_at"] = (
            datetime.now(timezone.utc).isoformat()
        )

        return True

    def has_consent(
        self,
        candidate_id: str,
        purpose: str,
    ) -> bool:
        record = self._consents.get(candidate_id)

        if not record:
            return False

        if not record["consent_given"]:
            return False

        return purpose in record["purposes"]

    def get_consent(self, candidate_id: str):
        return self._consents.get(candidate_id)