from stabilization.api_output_validator import (
    APIOutputValidator,
)


def test_success_response():
    validator = APIOutputValidator()

    response = validator.success_response(
        {"candidate_id": "CAND001"}
    )

    assert response["status"] == "success"
    assert response["data"]["candidate_id"] == "CAND001"


def test_error_response():
    validator = APIOutputValidator()

    response = validator.error_response(
        "Invalid candidate"
    )

    assert response["status"] == "error"


def test_invalid_response():
    validator = APIOutputValidator()

    try:
        validator.validate(
            {"status": "unknown"}
        )
        assert False
    except ValueError:
        assert True