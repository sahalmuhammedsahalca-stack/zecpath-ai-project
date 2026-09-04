from advanced_features.ai_coaching import AICoachingEngine


def test_ai_coaching():
    engine = AICoachingEngine()

    result = engine.generate_coaching(
        "CAND001",
        60,
        80,
        65,
    )

    assert result["candidate_id"] == "CAND001"
    assert len(result["coaching_suggestions"]) >= 1