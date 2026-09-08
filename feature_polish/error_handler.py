"""
Day 65 - Error Handling
"""


class FeatureErrorHandler:
    """Provide consistent error responses."""

    ERROR_MESSAGES = {
        "invalid_score": "The provided score is invalid.",
        "missing_candidate": "Candidate information is missing.",
        "invalid_candidate": "Candidate information is invalid.",
        "missing_report": "Report information is missing.",
    }

    def create_error(self, error_type, details=None):
        """Create a structured error response."""

        message = self.ERROR_MESSAGES.get(
            error_type,
            "An unexpected system error occurred.",
        )

        response = {
            "success": False,
            "error_type": error_type,
            "message": message,
        }

        if details:
            response["details"] = str(details)

        return response

    def create_success(self, data):
        """Create a consistent successful response."""

        return {
            "success": True,
            "data": data,
        }