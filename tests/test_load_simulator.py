from performance_scaling.load_simulator import LoadSimulator


def test_load_simulation():

    simulator = LoadSimulator(
        workers=3
    )

    result = simulator.run(
        lambda request: request * 2,
        list(range(10)),
    )

    assert result["request_count"] == 10
    assert result["successful_requests"] == 10
    assert result["failed_requests"] == 0
    assert result["throughput_per_second"] > 0