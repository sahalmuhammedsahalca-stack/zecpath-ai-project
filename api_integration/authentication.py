from typing import Dict, Any


class APIAuthentication:

    SUPPORTED_METHODS = {
        "API_KEY",
        "BEARER_TOKEN",
        "SERVICE_TOKEN",
    }

    @classmethod
    def validate_method(cls, method: str) -> bool:

        if method not in cls.SUPPORTED_METHODS:
            raise ValueError(
                f"Unsupported authentication method: {method}"
            )

        return True

    @staticmethod
    def create_security_policy() -> Dict[str, Any]:

        return {
            "authentication_required": True,
            "encryption_in_transit": True,
            "secret_storage": "environment_or_secret_manager",
            "logging_sensitive_values": False,
            "token_rotation": True,
            "least_privilege": True,
            "status": "proposed",
        }