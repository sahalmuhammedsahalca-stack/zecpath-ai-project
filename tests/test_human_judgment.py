from system_simulation.human_judgment import HumanJudgment


def test_record_human_judgment():
    judgment = HumanJudgment()

    record = judgment.record_judgment(
        "CAND001",
        90,
        "Highly Recommended",
    )

    assert record["candidate_id"] == "CAND001"
    assert record["human_score"] == 90


def test_compare_matching_decision():
    judgment = HumanJudgment()

    judgment.record_judgment(
        "CAND001",
        90,
        "Highly Recommended",
    )

    comparison = judgment.compare(
        "CAND001",
        88,
        "Highly Recommended",
    )

    assert comparison["decision_match"] is True
    assert comparison["score_difference"] == 2


def test_compare_different_decision():
    judgment = HumanJudgment()

    judgment.record_judgment(
        "CAND002",
        60,
        "Needs Review",
    )

    comparison = judgment.compare(
        "CAND002",
        85,
        "Highly Recommended",
    )

    assert comparison["decision_match"] is False
    assert comparison["score_difference"] == 25