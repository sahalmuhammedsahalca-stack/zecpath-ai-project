class MetricsTracker:
    def __init__(self):
        self.response_times = []
        self.accuracy_results = []
        self.total_requests = 0
        self.failed_requests = 0

    def record_response_time(self, response_time):
        self.response_times.append(float(response_time))
        self.total_requests += 1

    def record_accuracy(self, correct):
        self.accuracy_results.append(bool(correct))

    def record_failure(self):
        self.failed_requests += 1
        self.total_requests += 1

    def average_response_time(self):
        if not self.response_times:
            return 0.0

        return sum(self.response_times) / len(self.response_times)

    def accuracy(self):
        if not self.accuracy_results:
            return 0.0

        correct = sum(self.accuracy_results)
        return (correct / len(self.accuracy_results)) * 100

    def failure_rate(self):
        if self.total_requests == 0:
            return 0.0

        return (self.failed_requests / self.total_requests) * 100

    def summary(self):
        return {
            "total_requests": self.total_requests,
            "failed_requests": self.failed_requests,
            "average_response_time": round(
                self.average_response_time(), 6
            ),
            "accuracy_percent": round(self.accuracy(), 2),
            "failure_rate_percent": round(self.failure_rate(), 2),
        }