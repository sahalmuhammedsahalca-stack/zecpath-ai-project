from monitoring_observability.metrics_tracker import MetricsTracker


def test_metrics_tracker():
    metrics = MetricsTracker()

    metrics.record_response_time(0.2)
    metrics.record_response_time(0.4)

    metrics.record_accuracy(True)
    metrics.record_accuracy(True)
    metrics.record_accuracy(False)

    metrics.record_failure()

    summary = metrics.summary()

    assert summary["total_requests"] == 3
    assert summary["failed_requests"] == 1
    assert summary["average_response_time"] == 0.3
    assert summary["accuracy_percent"] == 66.67
    assert summary["failure_rate_percent"] == 33.33