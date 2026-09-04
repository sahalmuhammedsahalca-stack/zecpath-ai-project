import pytest

from advanced_features.realtime_feedback import RealTimeFeedbackEngine


def test_feedback_generation():
    engine = RealTimeFeedbackEngine()

    result = engine.generate_feedback(
        "CAND001",
        "communication",
        "Improve answer structure.",
        "medium",
    )

    assert result["candidate_id"] == "CAND001"
    assert result["priority"] == "medium"


def test_invalid_priority():
    engine = RealTimeFeedbackEngine()

    with pytest.raises(ValueError):
        engine.generate_feedback(
            "CAND001",
            "communication",
            "Improve answer structure.",
            "invalid",
        )