from system_simulation.full_system_simulator import (
    FullSystemSimulator,
)


def test_full_hiring_journey():
    simulator = FullSystemSimulator()

    candidate = {
        "candidate_id": "CAND001",
        "resume_file": "candidate001.pdf",
        "ats_score": 90,
        "screening_score": 85,
        "hr_score": 88,
        "technical_score": 92,
    }

    result = simulator.run(candidate)

    assert result["pipeline_status"] == "completed"
    assert result["stage_count"] == 6
    assert result["candidate_id"] == "CAND001"


def test_final_decision():
    simulator = FullSystemSimulator()

    candidate = {
        "candidate_id": "CAND002",
        "resume_file": "candidate002.pdf",
        "ats_score": 75,
        "screening_score": 72,
        "hr_score": 70,
        "technical_score": 73,
    }

    result = simulator.run(candidate)

    final_stage = result["stages"][-1]

    assert final_stage["decision"] == "Recommended"