"""
Day 65 - Scoring Consistency

Provides validation and normalization utilities for
candidate evaluation scores.
"""


class ScoringConsistency:
    """Validate and normalize candidate scores."""

    MIN_SCORE = 0
    MAX_SCORE = 100

    def validate_score(self, score):
        """Validate that a score is numeric and within range."""

        if not isinstance(score, (int, float)):
            raise ValueError("Score must be numeric.")

        if not self.MIN_SCORE <= score <= self.MAX_SCORE:
            raise ValueError("Score must be between 0 and 100.")

        return True

    def normalize_score(self, score):
        """Return a validated score rounded to two decimals."""

        self.validate_score(score)
        return round(float(score), 2)

    def normalize_scores(self, scores):
        """Normalize a collection of scores."""

        return {
            name: self.normalize_score(score)
            for name, score in scores.items()
        }

    def calculate_average(self, scores):
        """Calculate the average of validated scores."""

        if not scores:
            raise ValueError("At least one score is required.")

        normalized = self.normalize_scores(scores)

        return round(
            sum(normalized.values()) / len(normalized),
            2,
        )