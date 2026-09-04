from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class FeedbackEvent:
    candidate_id: str
    event_type: str
    message: str
    priority: str


class RealTimeFeedbackEngine:
    """
    Prototype real-time feedback engine.

    Future versions can receive streaming interview events from
    video/audio processing services.
    """

    PRIORITIES = {"low", "medium", "high"}

    def generate_feedback(
        self,
        candidate_id: str,
        event_type: str,
        message: str,
        priority: str = "medium",
    ) -> Dict[str, Any]:

        if not candidate_id:
            raise ValueError("candidate_id is required")

        if not event_type:
            raise ValueError("event_type is required")

        if not message:
            raise ValueError("message is required")

        if priority not in self.PRIORITIES:
            raise ValueError("Invalid feedback priority")

        event = FeedbackEvent(
            candidate_id=candidate_id,
            event_type=event_type,
            message=message,
            priority=priority,
        )

        return asdict(event)