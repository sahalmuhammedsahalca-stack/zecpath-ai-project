from security_governance.consent_manager import ConsentManager


def test_record_consent():
    manager = ConsentManager()

    record = manager.record_consent(
        "CAND001",
        [
            "recruitment_evaluation",
            "interview_analysis",
        ],
    )

    assert record["candidate_id"] == "CAND001"
    assert record["consent_given"] is True
    assert manager.has_consent(
        "CAND001",
        "recruitment_evaluation",
    )


def test_consent_restriction():
    manager = ConsentManager()

    manager.record_consent(
        "CAND001",
        ["recruitment_evaluation"],
    )

    assert manager.has_consent(
        "CAND001",
        "report_generation",
    ) is False


def test_revoke_consent():
    manager = ConsentManager()

    manager.record_consent(
        "CAND001",
        ["recruitment_evaluation"],
    )

    assert manager.revoke_consent("CAND001") is True

    assert manager.has_consent(
        "CAND001",
        "recruitment_evaluation",
    ) is False


def test_invalid_purpose():
    manager = ConsentManager()

    try:
        manager.record_consent(
            "CAND001",
            ["unknown_purpose"],
        )
        assert False
    except ValueError:
        assert True