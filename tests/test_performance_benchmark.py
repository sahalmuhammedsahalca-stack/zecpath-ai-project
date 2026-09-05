from performance_scaling.performance_benchmark import PerformanceBenchmark


def test_benchmark():

    benchmark = PerformanceBenchmark()

    result = benchmark.run(
        lambda value: value * 2,
        [1, 2, 3, 4],
        repetitions=2,
    )

    assert result["input_count"] == 4
    assert result["repetitions"] == 2
    assert result["average_time_seconds"] >= 0