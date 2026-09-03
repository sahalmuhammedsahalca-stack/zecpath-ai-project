from security_governance.access_control import AccessControl
from security_governance.audit_logger import AuditLogger
from security_governance.consent_manager import ConsentManager
from security_governance.data_retention import DataRetentionPolicy
from security_governance.secure_storage import SecureStorageManager


class GovernanceController:
    """
    Central controller for Zecpath AI security and governance checks.
    """

    def __init__(self, audit_directory=None):
        if audit_directory is None:
            audit_directory = "security_governance/audit_logs"

        self.audit_logger = AuditLogger(audit_directory)
        self.retention_policy = DataRetentionPolicy()
        self.consent_manager = ConsentManager()
        self.storage_manager = SecureStorageManager()
        self.access_control = AccessControl()

    def can_process_candidate(
        self,
        candidate_id: str,
        purpose: str,
    ) -> bool:
        return self.consent_manager.has_consent(
            candidate_id,
            purpose,
        )

    def can_access(
        self,
        role: str,
        permission: str,
    ) -> bool:
        return self.access_control.has_permission(
            role,
            permission,
        )

    def record_score(
        self,
        candidate_id: str,
        round_name: str,
        score: float,
        scoring_source: str,
    ):
        return self.audit_logger.log_score(
            candidate_id,
            round_name,
            score,
            scoring_source,
        )

    def record_decision(
        self,
        candidate_id: str,
        decision: str,
        confidence: float,
        decision_source: str,
    ):
        return self.audit_logger.log_decision(
            candidate_id,
            decision,
            confidence,
            decision_source,
        )