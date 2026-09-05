from performance_scaling.cache_manager import CacheManager


def test_cache_operations():

    cache = CacheManager()

    cache.set(
        "candidate_1",
        {"score": 90},
    )

    assert cache.get(
        "candidate_1"
    )["score"] == 90

    assert cache.size() == 1

    cache.delete("candidate_1")

    assert cache.get(
        "candidate_1"
    ) is None