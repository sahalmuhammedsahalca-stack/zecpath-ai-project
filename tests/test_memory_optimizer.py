from performance_scaling.memory_optimizer import MemoryOptimizer


def test_memory_comparison():

    optimizer = MemoryOptimizer()

    result = optimizer.compare(
        "a" * 100,
        "a",
    )

    assert result["before_bytes"] > 0
    assert result["after_bytes"] > 0