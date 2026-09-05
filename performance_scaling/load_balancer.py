from typing import List


class LoadBalancer:
    """Round-robin load balancer."""

    def __init__(
        self,
        instances: List[str],
    ):

        if not instances:
            raise ValueError(
                "At least one service instance is required"
            )

        self.instances = instances
        self.current_index = 0

    def next_instance(self):

        instance = self.instances[
            self.current_index
        ]

        self.current_index = (
            self.current_index + 1
        ) % len(self.instances)

        return instance

    def distribute(
        self,
        request_count: int,
    ):

        if request_count < 0:
            raise ValueError(
                "request_count cannot be negative"
            )

        distribution = {
            instance: 0
            for instance in self.instances
        }

        for _ in range(request_count):

            instance = self.next_instance()

            distribution[instance] += 1

        return distribution