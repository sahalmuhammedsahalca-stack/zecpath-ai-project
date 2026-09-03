from pathlib import Path

from security_governance.audit_logger import AuditLogger


def test_score_log(tmp_path):
    log_directory = tmp_path / "audit_logs"

    logger = AuditLogger(str(log_directory))

    record = logger.log_score(
        candidate_id="CAND001",
        round_name="technical",
        score=88.5,
        scoring_source="technical_scoring_engine",
    )

    assert record["event_type"] == "score"
    assert record["candidate_id"] == "CAND001"
    assert record["score"] == 88.5
    assert "timestamp" in record

    logs = logger.read_logs("score")

    assert len(logs) == 1
    assert logs[0]["candidate_id"] == "CAND001"


def test_decision_log(tmp_path):
    log_directory = tmp_path / "audit_logs"

    logger = AuditLogger(str(log_directory))

    record = logger.log_decision(
        candidate_id="CAND001",
        decision="Highly Recommended",
        confidence=92.5,
        decision_source="final_recommendation_engine",
    )

    assert record["event_type"] == "decision"
    assert record["candidate_id"] == "CAND001"
    assert record["decision"] == "Highly Recommended"
    assert record["confidence"] == 92.5
    assert "timestamp" in record

    logs = logger.read_logs("decision")

    assert len(logs) == 1
    assert logs[0]["candidate_id"] == "CAND001"