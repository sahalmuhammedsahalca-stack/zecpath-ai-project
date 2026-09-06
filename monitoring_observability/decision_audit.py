from datetime import datetime


class DecisionAuditLogger:
    def __init__(self):
        self.audit_logs = []

    def record_decision(
        self,
        candidate_id,
        score,
        recommendation,
        reason,
    ):
        record = {
            "timestamp": datetime.now().isoformat(),
            "candidate_id": candidate_id,
            "score": score,
            "recommendation": recommendation,
            "reason": reason,
        }

        self.audit_logs.append(record)
        return record

    def get_candidate_audit(self, candidate_id):
        return [
            record
            for record in self.audit_logs
            if record["candidate_id"] == candidate_id
        ]

    def get_all_audits(self):
        return self.audit_logs

    def count(self):
        return len(self.audit_logs)