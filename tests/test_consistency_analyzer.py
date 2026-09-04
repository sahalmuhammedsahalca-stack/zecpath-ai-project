from system_simulation.consistency_analyzer import (
    ConsistencyAnalyzer,
)


def test_consistent_result():
    analyzer = ConsistencyAnalyzer()

    comparison = {
        "candidate_id": "CAND001",
        "ai_score": 88,
        "human_score": 90,
        "score_difference": 2,
        "ai_decision": "Highly Recommended",
        "human_decision": "Highly Recommended",
        "decision_match": True,
    }

    result = analyzer.analyze(comparison)

    assert result["status"] == "Consistent"
    assert result["inconsistency_count"] == 0


def test_inconsistent_result():
    analyzer = ConsistencyAnalyzer()

    comparison = {
        "candidate_id": "CAND002",
        "ai_score": 90,
        "human_score": 65,
        "score_difference": 25,
        "ai_decision": "Highly Recommended",
        "human_decision": "Needs Review",
        "decision_match": False,
    }

    result = analyzer.analyze(comparison)

    assert result["status"] == "Inconsistent"
    assert result["inconsistency_count"] == 2