from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class EmotionResult:
    candidate_id: str
    dominant_emotion: str
    confidence: float
    status: str = "prototype"


class EmotionDetectionEngine:
    """
    Prototype interface for future emotion-analysis models.

    Emotion detection should be treated as an uncertain supporting signal,
    not as the sole basis for hiring decisions.
    """

    SUPPORTED_EMOTIONS = {
        "neutral",
        "positive",
        "negative",
        "uncertain",
    }

    def detect(
        self,
        candidate_id: str,
        dominant_emotion: str,
        confidence: float,
    ) -> Dict[str, Any]:

        if not candidate_id:
            raise ValueError("candidate_id is required")

        if dominant_emotion not in self.SUPPORTED_EMOTIONS:
            raise ValueError("Unsupported emotion category")

        if confidence < 0 or confidence > 100:
            raise ValueError("Confidence must be between 0 and 100")

        result = EmotionResult(
            candidate_id=candidate_id,
            dominant_emotion=dominant_emotion,
            confidence=confidence,
        )

        return asdict(result)