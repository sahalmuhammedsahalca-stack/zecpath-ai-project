from demo_dataset.simulation.demo_pipeline import DemoHiringPipeline


def test_demo_pipeline_candidate():
    pipeline = DemoHiringPipeline()

    result = pipeline.run_candidate("CAND001")

    assert result["status"] == "success"
    assert result["pipeline_completed"] is True
    assert result["results"]["ats_score"] == 92


def test_demo_pipeline_all_candidates():
    pipeline = DemoHiringPipeline()

    results = pipeline.run_all()

    assert len(results) == 3
    assert results["CAND001"]["status"] == "success"
    assert results["CAND002"]["status"] == "success"
    assert results["CAND003"]["status"] == "success"


def test_unknown_candidate():
    pipeline = DemoHiringPipeline()

    result = pipeline.run_candidate("CAND999")

    assert result["status"] == "error"