from performance_scaling.microservice_scaler import MicroserviceScaler


def test_scaling_decision():

    scaler = MicroserviceScaler(
        min_instances=1,
        max_instances=5,
        requests_per_instance=100,
    )

    assert scaler.required_instances(50) == 1
    assert scaler.required_instances(150) == 2
    assert scaler.required_instances(450) == 5