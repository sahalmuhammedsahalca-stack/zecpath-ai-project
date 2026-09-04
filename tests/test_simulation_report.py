from system_simulation.simulation_report import (
    SimulationReport,
)


def test_simulation_report():
    generator = SimulationReport()

    simulation = {
        "candidate_id": "CAND001",
        "pipeline_status": "completed",
        "stages": [
            {
                "decision": "Highly Recommended",
                "overall_score": 88,
            }
        ],
    }

    comparison = {
        "human_score": 90,
        "score_difference": 2,
        "decision_match": True,
    }

    consistency = {
        "status": "Consistent",
        "inconsistencies": [],
    }

    performance = {
        "completion_rate": 100,
    }

    report = generator.generate(
        simulation,
        comparison,
        consistency,
        performance,
    )

    assert report["candidate_id"] == "CAND001"
    assert report["ai_score"] == 88
    assert report["human_score"] == 90
    assert report["consistency_status"] == "Consistent"
    assert report["completion_rate"] == 100