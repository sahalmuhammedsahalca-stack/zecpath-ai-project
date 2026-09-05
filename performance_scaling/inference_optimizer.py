import time
from typing import Callable, Any


class InferenceOptimizer:
    """Measures AI inference execution performance."""

    def __init__(self):
        self.history = []

    def measure(
        self,
        model_function: Callable[[Any], Any],
        input_data: Any,
    ):
        start = time.perf_counter()

        result = model_function(input_data)

        elapsed = time.perf_counter() - start

        record = {
            "execution_time_seconds": round(elapsed, 6),
            "success": True,
        }

        self.history.append(record)

        return {
            "result": result,
            "performance": record,
        }

    def average_inference_time(self) -> float:
        if not self.history:
            return 0.0

        total = sum(
            item["execution_time_seconds"]
            for item in self.history
        )

        return round(
            total / len(self.history),
            6,
        )

    def optimization_summary(self):
        return {
            "runs": len(self.history),
            "average_inference_time_seconds":
                self.average_inference_time(),
        }