class MicroserviceScaler:
    """Determines required service instances."""

    def __init__(
        self,
        min_instances: int = 1,
        max_instances: int = 10,
        requests_per_instance: int = 100,
    ):

        if min_instances <= 0:
            raise ValueError(
                "min_instances must be positive"
            )

        if max_instances < min_instances:
            raise ValueError(
                "max_instances must be >= min_instances"
            )

        if requests_per_instance <= 0:
            raise ValueError(
                "requests_per_instance must be positive"
            )

        self.min_instances = min_instances
        self.max_instances = max_instances
        self.requests_per_instance = (
            requests_per_instance
        )

    def required_instances(
        self,
        requests: int,
    ):

        if requests < 0:
            raise ValueError(
                "requests cannot be negative"
            )

        calculated = (
            requests
            + self.requests_per_instance
            - 1
        ) // self.requests_per_instance

        return max(
            self.min_instances,
            min(
                calculated,
                self.max_instances,
            ),
        )

    def scaling_decision(
        self,
        requests: int,
    ):

        instances = self.required_instances(
            requests
        )

        if instances > self.min_instances:
            action = "scale_up"
        else:
            action = "maintain"

        return {
            "requests": requests,
            "required_instances": instances,
            "scaling_action": action,
        }