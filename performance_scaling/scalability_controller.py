class ScalabilityController:
    """Combines workload and scaling decisions."""

    def __init__(
        self,
        scaler,
    ):

        self.scaler = scaler

    def evaluate(
        self,
        request_count: int,
    ):

        decision = self.scaler.scaling_decision(
            request_count
        )

        if request_count == 0:
            status = "idle"

        elif (
            decision["required_instances"]
            == self.scaler.max_instances
        ):
            status = "maximum_capacity"

        else:
            status = "within_scaling_capacity"

        return {
            **decision,
            "capacity_status": status,
        }