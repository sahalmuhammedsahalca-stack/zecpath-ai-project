"""
Day 65 - Feature Polish Controller

Combines scoring, formatting, reporting, error handling
and recruiter-facing output improvements.
"""

from .scoring_consistency import ScoringConsistency
from .output_formatter import OutputFormatter
from .report_clarity import ReportClarity
from .error_handler import FeatureErrorHandler
from .recruiter_output import RecruiterOutput


class FeaturePolishController:
    """Coordinate Day 65 feature enhancements."""

    def __init__(self):
        self.scoring = ScoringConsistency()
        self.formatter = OutputFormatter()
        self.report = ReportClarity()
        self.errors = FeatureErrorHandler()
        self.recruiter = RecruiterOutput()

    def process_candidate(
        self,
        candidate_id,
        scores,
        recommendation,
        strengths=None,
        concerns=None,
    ):
        """Process and polish a candidate evaluation."""

        try:
            if not candidate_id:
                return self.errors.create_error(
                    "missing_candidate"
                )

            if not scores:
                return self.errors.create_error(
                    "invalid_score"
                )

            normalized_scores = self.scoring.normalize_scores(scores)
            overall_score = self.scoring.calculate_average(
                normalized_scores
            )

            candidate_card = self.recruiter.build_candidate_card(
                candidate_id,
                overall_score,
                recommendation,
                strengths,
                concerns,
            )

            return self.errors.create_success(
                {
                    "candidate": candidate_card,
                    "scores": normalized_scores,
                    "formatted_score": self.formatter.format_score(
                        overall_score
                    ),
                }
            )

        except ValueError as exc:
            return self.errors.create_error(
                "invalid_score",
                str(exc),
            )