from performance_scaling.load_balancer import LoadBalancer


def test_round_robin_distribution():

    balancer = LoadBalancer(
        [
            "service_1",
            "service_2",
            "service_3",
        ]
    )

    result = balancer.distribute(6)

    assert result == {
        "service_1": 2,
        "service_2": 2,
        "service_3": 2,
    }