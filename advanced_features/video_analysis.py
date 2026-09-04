from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class VideoAnalysisResult:
    candidate_id: str
    eye_contact_score: float
    speaking_activity_score: float
    engagement_score: float
    confidence_score: float
    status: str = "prototype"


class VideoAnalysisEngine:
    """
    Future-ready interface for AI video interview analysis.

    This prototype does not perform real facial recognition or video
    processing. It defines the structure that a future AI model can use.
    """

    def analyze(
        self,
        candidate_id: str,
        eye_contact_score: float,
        speaking_activity_score: float,
        engagement_score: float,
        confidence_score: float,
    ) -> Dict[str, Any]:

        if not candidate_id:
            raise ValueError("candidate_id is required")

        scores = [
            eye_contact_score,
            speaking_activity_score,
            engagement_score,
            confidence_score,
        ]

        if any(score < 0 or score > 100 for score in scores):
            raise ValueError("Video analysis scores must be between 0 and 100")

        result = VideoAnalysisResult(
            candidate_id=candidate_id,
            eye_contact_score=eye_contact_score,
            speaking_activity_score=speaking_activity_score,
            engagement_score=engagement_score,
            confidence_score=confidence_score,
        )

        return asdict(result)