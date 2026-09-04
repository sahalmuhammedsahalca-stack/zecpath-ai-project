from typing import Dict, Any


class RetryPolicy:

    DEFAULT_MAX_RETRIES = 3

    RETRYABLE_ERRORS = {
        "TIMEOUT",
        "TEMPORARY_UNAVAILABLE",
        "RATE_LIMITED",
        "CONNECTION_ERROR",
    }

    @classmethod
    def should_retry(
        cls,
        error_code: str,
        attempt: int,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> bool:

        if attempt >= max_retries:
            return False

        return error_code in cls.RETRYABLE_ERRORS


class APIErrorHandler:

    @staticmethod
    def create_error(
        error_code: str,
        message: str,
        retryable: bool,
    ) -> Dict[str, Any]:

        return {
            "success": False,
            "error": {
                "code": error_code,
                "message": message,
                "retryable": retryable,
            },
        }