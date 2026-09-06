from datetime import datetime


class ObservabilityLogger:
    def __init__(self):
        self.logs = []

    def _record(self, log_type, data):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": log_type,
            "data": data,
        }
        self.logs.append(entry)
        return entry

    def log_api(self, endpoint, method, status, response_time):
        return self._record(
            "api",
            {
                "endpoint": endpoint,
                "method": method,
                "status": status,
                "response_time": response_time,
            },
        )

    def log_model_output(self, model, output, score=None):
        return self._record(
            "model_output",
            {
                "model": model,
                "output": output,
                "score": score,
            },
        )

    def log_error(self, error_type, message):
        return self._record(
            "error",
            {
                "error_type": error_type,
                "message": message,
            },
        )

    def get_logs(self, log_type=None):
        if log_type is None:
            return self.logs

        return [log for log in self.logs if log["type"] == log_type]

    def count(self):
        return len(self.logs)