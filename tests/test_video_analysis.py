import pytest

from advanced_features.video_analysis import VideoAnalysisEngine


def test_video_analysis():
    engine = VideoAnalysisEngine()

    result = engine.analyze(
        "CAND001",
        80,
        75,
        82,
        78,
    )

    assert result["candidate_id"] == "CAND001"
    assert result["eye_contact_score"] == 80
    assert result["status"] == "prototype"


def test_video_analysis_invalid_score():
    engine = VideoAnalysisEngine()

    with pytest.raises(ValueError):
        engine.analyze(
            "CAND001",
            101,
            75,
            82,
            78,
        )