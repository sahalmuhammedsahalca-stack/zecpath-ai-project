from typing import Dict, Any


class InterviewAnalyticsEngine:
    """
    Produces structured analytics suitable for a future dashboard.
    """

    def generate_dashboard_data(
        self,
        candidate_id: str,
        technical_score: float,
        behavioral_score: float,
        communication_score: float,
        overall_score: float,
    ) -> Dict[str, Any]:

        scores = {
            "technical": technical_score,
            "behavioral": behavioral_score,
            "communication": communication_score,
            "overall": overall_score,
        }

        if any(score < 0 or score > 100 for score in scores.values()):
            raise ValueError("Scores must be between 0 and 100")

        return {
            "candidate_id": candidate_id,
            "metrics": scores,
            "dashboard_sections": [
                "Overall Performance",
                "Technical Performance",
                "Behavioral Performance",
                "Communication Performance",
                "Improvement Areas",
                "Interview Trend",
            ],
            "status": "prototype",
        }