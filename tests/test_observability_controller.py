from monitoring_observability.observability_controller import (
    ObservabilityController,
)


def test_observability_controller():
    controller = ObservabilityController()

    controller.record_api_request(
        "/api/v1/resume/parse",
        "POST",
        "success",
        0.25,
    )

    controller.record_model_result(
        "ats-model",
        "Recommended",
        85,
    )

    controller.record_accuracy(True)

    controller.record_decision(
        "CAND001",
        85,
        "Recommended",
        "Good candidate fit",
    )

    report = controller.get_monitoring_report(
        {
            "total_candidates": 10,
            "successful": 9,
            "failed": 1,
        },
        {
            "total_interviews": 5,
            "successful_interviews": 4,
            "success_rate_percent": 80.0,
        },
    )

    assert report["metrics"]["total_requests"] == 1
    assert report["log_count"] == 2
    assert report["audit_log_count"] == 1