class ScoringStabilizer:
    """
    Validates and stabilizes AI scoring outputs.
    """

    MIN_SCORE = 0
    MAX_SCORE = 100

    def normalize_score(self, score):
        if score is None:
            raise ValueError("Score cannot be None")

        try:
            score = float(score)
        except (TypeError, ValueError):
            raise ValueError("Score must be numeric")

        return round(
            max(self.MIN_SCORE, min(self.MAX_SCORE, score)),
            2,
        )

    def validate_score(self, score):
        normalized_score = self.normalize_score(score)

        return {
            "valid": True,
            "score": normalized_score,
        }

    def calculate_average(self, scores):
        if not scores:
            raise ValueError("Scores cannot be empty")

        normalized_scores = [
            self.normalize_score(score)
            for score in scores
        ]

        return round(
            sum(normalized_scores) / len(normalized_scores),
            2,
        )

    def check_consistency(self, scores, threshold=20):
        if not scores:
            raise ValueError("Scores cannot be empty")

        normalized_scores = [
            self.normalize_score(score)
            for score in scores
        ]

        variation = max(normalized_scores) - min(
            normalized_scores
        )

        return {
            "scores": normalized_scores,
            "variation": round(variation, 2),
            "consistent": variation <= threshold,
        }