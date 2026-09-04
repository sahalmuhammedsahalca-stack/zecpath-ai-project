from typing import Dict, Any


class RequestSchemaValidator:

    REQUIRED_FIELDS = {
        "resume_parsing": {"candidate_id", "resume_path"},
        "ats_scoring": {"candidate_id", "resume_data", "job_description"},
        "screening": {"candidate_id", "resume_score", "screening_questions"},
        "interview": {"candidate_id", "interview_id", "responses"},
        "decision": {
            "candidate_id",
            "ats_score",
            "screening_score",
            "interview_score",
        },
    }

    @classmethod
    def validate(
        cls,
        api_name: str,
        payload: Dict[str, Any],
    ) -> bool:

        if api_name not in cls.REQUIRED_FIELDS:
            raise KeyError(f"Unknown API: {api_name}")

        if not isinstance(payload, dict):
            raise TypeError("Request payload must be a dictionary")

        required = cls.REQUIRED_FIELDS[api_name]

        missing = required - payload.keys()

        if missing:
            raise ValueError(
                f"Missing required fields: {sorted(missing)}"
            )

        return True


class ResponseSchemaBuilder:

    @staticmethod
    def success(
        request_id: str,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:

        return {
            "success": True,
            "request_id": request_id,
            "data": data,
            "error": None,
        }

    @staticmethod
    def error(
        request_id: str,
        error_code: str,
        message: str,
    ) -> Dict[str, Any]:

        return {
            "success": False,
            "request_id": request_id,
            "data": None,
            "error": {
                "code": error_code,
                "message": message,
            },
        }