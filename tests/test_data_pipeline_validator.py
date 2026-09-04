from stabilization.data_pipeline_validator import (
    DataPipelineValidator,
)


def test_candidate_validation():
    validator = DataPipelineValidator()

    assert validator.validate_candidate(
        {"candidate_id": "CAND001"}
    ) is True


def test_missing_candidate_id():
    validator = DataPipelineValidator()

    try:
        validator.validate_candidate({})
        assert False
    except ValueError:
        assert True


def test_score_validation():
    validator = DataPipelineValidator()

    assert validator.validate_score_data(
        {
            "candidate_id": "CAND001",
            "score": 85,
        }
    ) is True


def test_invalid_score():
    validator = DataPipelineValidator()

    try:
        validator.validate_score_data(
            {
                "candidate_id": "CAND001",
                "score": 120,
            }
        )
        assert False
    except ValueError:
        assert True


def test_pipeline_record():
    validator = DataPipelineValidator()

    assert validator.validate_pipeline_record(
        {
            "candidate_id": "CAND001",
            "stage": "screening",
            "status": "completed",
        }
    ) is True