import pytest

from advanced_features.interview_analytics import InterviewAnalyticsEngine


def test_interview_analytics():
    engine = InterviewAnalyticsEngine()

    result = engine.generate_dashboard_data(
        "CAND001",
        80,
        75,
        70,
        75,
    )

    assert result["candidate_id"] == "CAND001"
    assert result["metrics"]["overall"] == 75
    assert "Overall Performance" in result["dashboard_sections"]


def test_invalid_score():
    engine = InterviewAnalyticsEngine()

    with pytest.raises(ValueError):
        engine.generate_dashboard_data(
            "CAND001",
            110,
            75,
            70,
            75,
        )