import time
from typing import Callable, Any


class APILatencyOptimizer:
    """Measures API response latency."""

    def __init__(self):
        self.measurements = []

    def execute(
        self,
        api_function: Callable[[Any], Any],
        request: Any,
    ):
        start = time.perf_counter()

        try:
            response = api_function(request)
            success = True

        except Exception as exc:
            response = {
                "status": "error",
                "message": str(exc),
            }
            success = False

        latency = time.perf_counter() - start

        record = {
            "latency_seconds": round(
                latency,
                6,
            ),
            "success": success,
        }

        self.measurements.append(record)

        return {
            "response": response,
            "performance": record,
        }

    def average_latency(self):
        if not self.measurements:
            return 0.0

        total = sum(
            item["latency_seconds"]
            for item in self.measurements
        )

        return round(
            total / len(self.measurements),
            6,
        )

    def summary(self):
        return {
            "request_count": len(self.measurements),
            "average_latency_seconds":
                self.average_latency(),
        }