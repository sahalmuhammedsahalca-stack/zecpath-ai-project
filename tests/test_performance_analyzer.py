from system_simulation.performance_analyzer import (
    PerformanceAnalyzer,
)


def test_pipeline_performance():
    analyzer = PerformanceAnalyzer()

    simulation = {
        "candidate_id": "CAND001",
        "stage_count": 6,
        "pipeline_status": "completed",
        "stages": [
            {"status": "completed"},
            {"status": "completed"},
            {"status": "passed"},
            {"status": "completed"},
            {"status": "completed"},
            {"status": "completed"},
        ],
    }

    result = analyzer.analyze(simulation)

    assert result["total_stages"] == 6
    assert result["completed_stages"] == 6
    assert result["completion_rate"] == 100