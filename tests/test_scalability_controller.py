from performance_scaling.microservice_scaler import MicroserviceScaler
from performance_scaling.scalability_controller import ScalabilityController


def test_scalability_controller():

    scaler = MicroserviceScaler(
        min_instances=1,
        max_instances=5,
        requests_per_instance=100,
    )

    controller = ScalabilityController(
        scaler
    )

    result = controller.evaluate(250)

    assert result["required_instances"] == 3
    assert (
        result["capacity_status"]
        == "within_scaling_capacity"
    )