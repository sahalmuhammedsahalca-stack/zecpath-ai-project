"""
Day 65 - Recruiter-Facing Output
"""


class RecruiterOutput:
    """Create concise recruiter-facing candidate outputs."""

    def build_candidate_card(
        self,
        candidate_id,
        overall_score,
        recommendation,
        strengths=None,
        concerns=None,
    ):
        """Build a recruiter-friendly candidate summary."""

        return {
            "candidate_id": candidate_id,
            "overall_score": round(float(overall_score), 2),
            "recommendation": recommendation,
            "strengths": strengths or [],
            "concerns": concerns or [],
        }

    def build_ranked_candidates(self, candidates):
        """Sort candidates by overall score."""

        return sorted(
            candidates,
            key=lambda candidate: candidate["overall_score"],
            reverse=True,
        )