from typing import Dict, Any, List


class AICoachingEngine:
    """
    Generates structured coaching recommendations from interview scores.
    """

    def generate_coaching(
        self,
        candidate_id: str,
        technical_score: float,
        behavioral_score: float,
        communication_score: float,
    ) -> Dict[str, Any]:

        if not candidate_id:
            raise ValueError("candidate_id is required")

        scores = {
            "technical": technical_score,
            "behavioral": behavioral_score,
            "communication": communication_score,
        }

        if any(score < 0 or score > 100 for score in scores.values()):
            raise ValueError("Scores must be between 0 and 100")

        suggestions: List[str] = []

        if technical_score < 70:
            suggestions.append(
                "Improve technical fundamentals and practice role-specific problems."
            )

        if behavioral_score < 70:
            suggestions.append(
                "Practice structured answers for behavioral interview questions."
            )

        if communication_score < 70:
            suggestions.append(
                "Improve answer clarity, structure, and communication confidence."
            )

        if not suggestions:
            suggestions.append(
                "Maintain current performance and continue regular interview practice."
            )

        return {
            "candidate_id": candidate_id,
            "scores": scores,
            "coaching_suggestions": suggestions,
            "status": "prototype",
        }