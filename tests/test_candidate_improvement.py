from advanced_features.candidate_improvement import CandidateImprovementEngine


def test_candidate_improvement():
    engine = CandidateImprovementEngine()

    result = engine.identify_improvements(
        "CAND001",
        {
            "technical": 55,
            "behavioral": 80,
            "communication": 68,
        },
    )

    assert result["candidate_id"] == "CAND001"
    assert len(result["improvement_areas"]) == 2