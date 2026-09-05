import time


class PerformanceBenchmark:
    """Runs repeatable performance benchmarks."""

    def run(
        self,
        function,
        inputs,
        repetitions: int = 1,
    ):

        if repetitions <= 0:
            raise ValueError(
                "repetitions must be greater than zero"
            )

        measurements = []

        for _ in range(repetitions):

            start = time.perf_counter()

            for item in inputs:
                function(item)

            elapsed = (
                time.perf_counter() - start
            )

            measurements.append(elapsed)

        average = (
            sum(measurements)
            / len(measurements)
        )

        return {
            "input_count": len(inputs),
            "repetitions": repetitions,
            "average_time_seconds":
                round(average, 6),
            "minimum_time_seconds":
                round(min(measurements), 6),
            "maximum_time_seconds":
                round(max(measurements), 6),
        }