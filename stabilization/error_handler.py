from datetime import datetime, timezone


class ErrorHandler:
    """
    Provides consistent error handling and structured
    error responses.
    """

    ERROR_MESSAGES = {
        ValueError: "Invalid input data",
        TypeError: "Invalid data type",
        KeyError: "Required data field is missing",
        PermissionError: "Access denied",
    }

    def create_error_response(self, error):
        message = self.ERROR_MESSAGES.get(
            type(error),
            "Unexpected system error",
        )

        return {
            "status": "error",
            "error_type": type(error).__name__,
            "message": message,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
        }

    def handle(self, error):
        return self.create_error_response(error)