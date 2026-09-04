class EdgeCaseValidator:
    """
    Handles common edge cases in AI recruitment processing.
    """

    def validate_candidate_id(self, candidate_id):
        if candidate_id is None:
            return False

        if not isinstance(candidate_id, str):
            return False

        return bool(candidate_id.strip())

    def validate_score(self, score):
        if score is None:
            return False

        if not isinstance(score, (int, float)):
            return False

        return 0 <= score <= 100

    def validate_text(self, text):
        if text is None:
            return False

        if not isinstance(text, str):
            return False

        return bool(text.strip())

    def validate_list(self, values):
        if values is None:
            return False

        if not isinstance(values, list):
            return False

        return len(values) > 0