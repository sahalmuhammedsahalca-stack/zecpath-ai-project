class HumanJudgment:
    """
    Stores and compares human hiring judgment with AI decisions.
    """

    def __init__(self):
        self.judgments = {}

    def record_judgment(
        self,
        candidate_id,
        score,
        decision,
    ):
        record = {
            "candidate_id": candidate_id,
            "human_score": score,
            "human_decision": decision,
        }

        self.judgments[candidate_id] = record

        return record

    def get_judgment(self, candidate_id):
        return self.judgments.get(candidate_id)

    def compare(
        self,
        candidate_id,
        ai_score,
        ai_decision,
    ):
        human = self.get_judgment(candidate_id)

        if human is None:
            raise ValueError(
                f"No human judgment found for {candidate_id}"
            )

        score_difference = abs(
            ai_score - human["human_score"]
        )

        decision_match = (
            ai_decision == human["human_decision"]
        )

        return {
            "candidate_id": candidate_id,
            "ai_score": ai_score,
            "human_score": human["human_score"],
            "score_difference": round(score_difference, 2),
            "ai_decision": ai_decision,
            "human_decision": human["human_decision"],
            "decision_match": decision_match,
        }