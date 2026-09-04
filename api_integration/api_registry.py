from typing import Dict, Any


class APIRegistry:
    """
    Central registry for Zecpath AI service endpoints.

    These are logical API definitions for integration planning.
    They do not represent live production endpoints.
    """

    APIS = {
        "resume_parsing": {
            "name": "Resume Parsing API",
            "method": "POST",
            "path": "/api/v1/resume/parse",
            "processing": "async",
            "service": "resume_parser",
        },
        "ats_scoring": {
            "name": "ATS Scoring API",
            "method": "POST",
            "path": "/api/v1/ats/score",
            "processing": "async",
            "service": "ats_scoring",
        },
        "screening": {
            "name": "Screening AI API",
            "method": "POST",
            "path": "/api/v1/screening/evaluate",
            "processing": "async",
            "service": "screening_ai",
        },
        "interview": {
            "name": "Interview AI API",
            "method": "POST",
            "path": "/api/v1/interview/score",
            "processing": "sync",
            "service": "interview_ai",
        },
        "decision": {
            "name": "Decision AI API",
            "method": "POST",
            "path": "/api/v1/decision/recommend",
            "processing": "sync",
            "service": "decision_ai",
        },
    }

    @classmethod
    def get_api(cls, api_name: str) -> Dict[str, Any]:
        if api_name not in cls.APIS:
            raise KeyError(f"Unknown API: {api_name}")

        return cls.APIS[api_name]

    @classmethod
    def list_apis(cls) -> Dict[str, Dict[str, Any]]:
        return cls.APIS.copy()