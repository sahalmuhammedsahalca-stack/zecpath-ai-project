class DataPipelineValidator:
    """
    Validates candidate data as it moves through
    the AI processing pipeline.
    """

    REQUIRED_FIELDS = {
        "candidate_id",
    }

    def validate_candidate(self, candidate):
        if not isinstance(candidate, dict):
            raise ValueError(
                "Candidate data must be a dictionary"
            )

        missing_fields = [
            field
            for field in self.REQUIRED_FIELDS
            if not candidate.get(field)
        ]

        if missing_fields:
            raise ValueError(
                f"Missing required fields: {missing_fields}"
            )

        return True

    def validate_score_data(self, candidate):
        self.validate_candidate(candidate)

        if "score" not in candidate:
            raise ValueError(
                "Candidate score is missing"
            )

        score = candidate["score"]

        if not isinstance(score, (int, float)):
            raise ValueError(
                "Candidate score must be numeric"
            )

        if score < 0 or score > 100:
            raise ValueError(
                "Candidate score must be between 0 and 100"
            )

        return True

    def validate_pipeline_record(self, record):
        if not isinstance(record, dict):
            raise ValueError(
                "Pipeline record must be a dictionary"
            )

        required_fields = {
            "candidate_id",
            "stage",
            "status",
        }

        missing_fields = [
            field
            for field in required_fields
            if not record.get(field)
        ]

        if missing_fields:
            raise ValueError(
                f"Missing pipeline fields: {missing_fields}"
            )

        return True