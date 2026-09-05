import time
from concurrent.futures import ThreadPoolExecutor


class LoadSimulator:
    """Simulates concurrent AI service requests."""

    def __init__(
        self,
        workers: int = 5,
    ):

        if workers <= 0:
            raise ValueError(
                "workers must be positive"
            )

        self.workers = workers

    def _execute(
        self,
        function,
        request,
    ):

        start = time.perf_counter()

        try:
            function(request)
            success = True

        except Exception:
            success = False

        elapsed = time.perf_counter() - start

        return {
            "success": success,
            "latency_seconds": elapsed,
        }

    def run(
        self,
        function,
        requests,
    ):

        start = time.perf_counter()

        with ThreadPoolExecutor(
            max_workers=self.workers
        ) as executor:

            results = list(
                executor.map(
                    lambda request:
                        self._execute(
                            function,
                            request,
                        ),
                    requests,
                )
            )

        total_time = (
            time.perf_counter() - start
        )

        successful = sum(
            result["success"]
            for result in results
        )

        return {
            "request_count": len(requests),
            "successful_requests": successful,
            "failed_requests":
                len(requests) - successful,
            "total_time_seconds":
                round(total_time, 6),
            "throughput_per_second":
                round(
                    len(requests) / total_time,
                    3,
                )
                if total_time > 0
                else 0,
        }