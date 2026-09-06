from monitoring_observability.decision_audit import DecisionAuditLogger


def test_decision_audit():
    audit = DecisionAuditLogger()

    record = audit.record_decision(
        "CAND001",
        88,
        "Highly Recommended",
        "Strong overall performance",
    )

    assert record["candidate_id"] == "CAND001"
    assert record["score"] == 88
    assert audit.count() == 1

    candidate_logs = audit.get_candidate_audit("CAND001")

    assert len(candidate_logs) == 1