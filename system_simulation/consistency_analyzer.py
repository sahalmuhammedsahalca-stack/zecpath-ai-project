class ConsistencyAnalyzer:
    """
    Identifies differences between AI and human judgment.
    """

    def analyze(self, comparison):
        inconsistencies = []

        if comparison["score_difference"] > 10:
            inconsistencies.append(
                "Significant score difference"
            )

        if not comparison["decision_match"]:
            inconsistencies.append(
                "AI and human decisions differ"
            )

        if inconsistencies:
            status = "Inconsistent"
        else:
            status = "Consistent"

        return {
            "candidate_id": comparison["candidate_id"],
            "status": status,
            "inconsistencies": inconsistencies,
            "inconsistency_count": len(inconsistencies),
        }