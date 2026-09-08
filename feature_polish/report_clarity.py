"""
Day 65 - Report Clarity
"""


class ReportClarity:
    """Generate clear recruiter-facing report sections."""

    def create_section(self, title, content):
        """Create a structured report section."""

        if not title or not str(title).strip():
            raise ValueError("Report section title is required.")

        if content is None:
            raise ValueError("Report section content is required.")

        return {
            "title": str(title).strip(),
            "content": str(content).strip(),
        }

    def create_candidate_summary(
        self,
        candidate_id,
        strengths,
        concerns,
        recommendation,
    ):
        """Create a concise candidate summary."""

        return {
            "candidate_id": candidate_id,
            "strengths": list(strengths),
            "concerns": list(concerns),
            "recommendation": recommendation,
        }