class AlertManager:
    def __init__(
        self,
        max_response_time=1.0,
        min_accuracy=80.0,
        max_failure_rate=10.0,
    ):
        self.max_response_time = max_response_time
        self.min_accuracy = min_accuracy
        self.max_failure_rate = max_failure_rate

    def check_response_time(self, response_time):
        if response_time > self.max_response_time:
            return {
                "alert": True,
                "type": "HIGH_RESPONSE_TIME",
                "value": response_time,
            }

        return {
            "alert": False,
            "type": "HIGH_RESPONSE_TIME",
            "value": response_time,
        }

    def check_accuracy(self, accuracy):
        if accuracy < self.min_accuracy:
            return {
                "alert": True,
                "type": "LOW_ACCURACY",
                "value": accuracy,
            }

        return {
            "alert": False,
            "type": "LOW_ACCURACY",
            "value": accuracy,
        }

    def check_failure_rate(self, failure_rate):
        if failure_rate > self.max_failure_rate:
            return {
                "alert": True,
                "type": "HIGH_FAILURE_RATE",
                "value": failure_rate,
            }

        return {
            "alert": False,
            "type": "HIGH_FAILURE_RATE",
            "value": failure_rate,
        }

    def evaluate(self, metrics):
        alerts = [
            self.check_response_time(metrics["average_response_time"]),
            self.check_accuracy(metrics["accuracy_percent"]),
            self.check_failure_rate(metrics["failure_rate_percent"]),
        ]

        return {
            "alerts": alerts,
            "alert_count": sum(alert["alert"] for alert in alerts),
        }