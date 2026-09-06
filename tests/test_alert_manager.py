from monitoring_observability.alert_manager import AlertManager


def test_alert_manager():
    manager = AlertManager(
        max_response_time=1.0,
        min_accuracy=80.0,
        max_failure_rate=10.0,
    )

    assert manager.check_response_time(2.0)["alert"] is True
    assert manager.check_accuracy(70.0)["alert"] is True
    assert manager.check_failure_rate(20.0)["alert"] is True

    report = manager.evaluate(
        {
            "average_response_time": 0.2,
            "accuracy_percent": 90.0,
            "failure_rate_percent": 2.0,
        }
    )

    assert report["alert_count"] == 0