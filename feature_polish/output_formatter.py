"""
Day 65 - Output Readability
"""


class OutputFormatter:
    """Format candidate evaluation results for readability."""

    def format_score(self, score):
        """Format a score consistently."""

        return f"{float(score):.2f}/100"

    def format_candidate_result(
        self,
        candidate_id,
        score,
        recommendation,
    ):
        """Create a recruiter-friendly candidate result."""

        return {
            "candidate_id": candidate_id,
            "score": self.format_score(score),
            "recommendation": recommendation,
        }

    def format_summary(self, candidate_results):
        """Create a readable summary for multiple candidates."""

        return [
            self.format_candidate_result(
                result["candidate_id"],
                result["score"],
                result["recommendation"],
            )
            for result in candidate_results
        ]