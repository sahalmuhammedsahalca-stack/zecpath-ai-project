from security_governance.governance_controller import GovernanceController


def test_candidate_processing_requires_consent(tmp_path):
    controller = GovernanceController(
        audit_directory=str(tmp_path / "audit")
    )

    assert controller.can_process_candidate(
        "CAND001",
        "recruitment_evaluation",
    ) is False

    controller.consent_manager.record_consent(
        "CAND001",
        ["recruitment_evaluation"],
    )

    assert controller.can_process_candidate(
        "CAND001",
        "recruitment_evaluation",
    ) is True


def test_role_access(tmp_path):
    controller = GovernanceController(
        audit_directory=str(tmp_path / "audit")
    )

    assert controller.can_access(
        "admin",
        "view_audit_logs",
    ) is True

    assert controller.can_access(
        "recruiter",
        "view_transcripts",
    ) is False


def test_governance_score_logging(tmp_path):
    controller = GovernanceController(
        audit_directory=str(tmp_path / "audit")
    )

    record = controller.record_score(
        "CAND001",
        "technical",
        90.0,
        "technical_scoring_engine",
    )

    assert record["candidate_id"] == "CAND001"
    assert record["score"] == 90.0


def test_governance_decision_logging(tmp_path):
    controller = GovernanceController(
        audit_directory=str(tmp_path / "audit")
    )

    record = controller.record_decision(
        "CAND001",
        "Highly Recommended",
        91.0,
        "final_recommendation_engine",
    )

    assert record["candidate_id"] == "CAND001"
    assert record["decision"] == "Highly Recommended"