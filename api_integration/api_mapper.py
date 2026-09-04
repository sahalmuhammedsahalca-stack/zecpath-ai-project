from typing import Dict, Any


class APIMapper:
    """
    Defines backend -> AI -> database integration relationships.
    """

    MAPPINGS = {
        "resume_parsing": {
            "input_source": "backend",
            "ai_service": "resume_parser",
            "database_target": "parsed_resumes",
            "processing": "async",
        },
        "ats_scoring": {
            "input_source": "backend",
            "ai_service": "ats_scoring",
            "database_target": "ats_scores",
            "processing": "async",
        },
        "screening": {
            "input_source": "backend",
            "ai_service": "screening_ai",
            "database_target": "screening_results",
            "processing": "async",
        },
        "interview": {
            "input_source": "backend",
            "ai_service": "interview_ai",
            "database_target": "interview_scores",
            "processing": "sync",
        },
        "decision": {
            "input_source": "backend",
            "ai_service": "decision_ai",
            "database_target": "final_recommendations",
            "processing": "sync",
        },
    }

    @classmethod
    def get_mapping(cls, api_name: str) -> Dict[str, Any]:
        if api_name not in cls.MAPPINGS:
            raise KeyError(f"Unknown API mapping: {api_name}")

        return cls.MAPPINGS[api_name]

    @classmethod
    def validate_mapping(cls, api_name: str) -> bool:
        mapping = cls.get_mapping(api_name)

        required_fields = {
            "input_source",
            "ai_service",
            "database_target",
            "processing",
        }

        return required_fields.issubset(mapping.keys())