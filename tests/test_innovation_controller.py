from advanced_features.innovation_controller import InnovationController


def test_innovation_controller():
    controller = InnovationController()

    result = controller.generate_feature_proposal("CAND001")

    assert result["candidate_id"] == "CAND001"
    assert "video_analysis" in result
    assert "emotion_detection" in result
    assert "real_time_feedback" in result
    assert "ai_coaching" in result
    assert "candidate_improvement" in result
    assert "interview_analytics" in result
    assert "roadmap" in result