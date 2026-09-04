from typing import Dict, Any, List


class CandidateImprovementEngine:
    """
    Identifies candidate development areas from interview performance.
    """

    def identify_improvements(
        self,
        candidate_id: str,
        scores: Dict[str, float],
    ) -> Dict[str, Any]:

        if not candidate_id:
            raise ValueError("candidate_id is required")

        if not scores:
            raise ValueError("scores are required")

        improvement_areas: List[str] = []

        for category, score in scores.items():

            if score < 60:
                improvement_areas.append(
                    f"High priority improvement required in {category}."
                )

            elif score < 75:
                improvement_areas.append(
                    f"Moderate improvement recommended in {category}."
                )

        if not improvement_areas:
            improvement_areas.append(
                "No major improvement area identified."
            )

        return {
            "candidate_id": candidate_id,
            "improvement_areas": improvement_areas,
            "status": "prototype",
        }