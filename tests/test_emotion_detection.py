import pytest

from advanced_features.emotion_detection import EmotionDetectionEngine


def test_emotion_detection():
    engine = EmotionDetectionEngine()

    result = engine.detect(
        "CAND001",
        "neutral",
        80,
    )

    assert result["candidate_id"] == "CAND001"
    assert result["dominant_emotion"] == "neutral"


def test_invalid_emotion():
    engine = EmotionDetectionEngine()

    with pytest.raises(ValueError):
        engine.detect(
            "CAND001",
            "unknown_emotion",
            80,
        )