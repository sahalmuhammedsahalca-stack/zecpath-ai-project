from monitoring_observability.logging_system import ObservabilityLogger


def test_logging_system():
    logger = ObservabilityLogger()

    api_log = logger.log_api(
        "/api/test",
        "POST",
        "success",
        0.25,
    )

    model_log = logger.log_model_output(
        "screening-model",
        "Recommended",
        88,
    )

    error_log = logger.log_error(
        "TIMEOUT",
        "Model request timed out",
    )

    assert api_log["type"] == "api"
    assert model_log["type"] == "model_output"
    assert error_log["type"] == "error"
    assert logger.count() == 3