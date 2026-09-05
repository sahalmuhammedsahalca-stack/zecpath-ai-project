from performance_scaling.api_latency_optimizer import APILatencyOptimizer


def test_api_latency():

    optimizer = APILatencyOptimizer()

    result = optimizer.execute(
        lambda request: {"status": "success"},
        {},
    )

    assert result["response"]["status"] == "success"
    assert result["performance"]["success"] is True
    assert optimizer.average_latency() >= 0