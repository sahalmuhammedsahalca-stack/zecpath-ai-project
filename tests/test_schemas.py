import pytest

from api_integration.schemas import (
    RequestSchemaValidator,
    ResponseSchemaBuilder,
)


def test_valid_resume_request():

    payload = {
        "candidate_id": "CAND001",
        "resume_path": "resume.pdf",
    }

    assert RequestSchemaValidator.validate(
        "resume_parsing",
        payload,
    )


def test_missing_request_field():

    payload = {
        "candidate_id": "CAND001",
    }

    with pytest.raises(ValueError):
        RequestSchemaValidator.validate(
            "resume_parsing",
            payload,
        )


def test_success_response():

    response = ResponseSchemaBuilder.success(
        "REQ001",
        {"score": 85},
    )

    assert response["success"] is True
    assert response["request_id"] == "REQ001"


def test_error_response():

    response = ResponseSchemaBuilder.error(
        "REQ001",
        "INVALID_REQUEST",
        "Invalid payload",
    )

    assert response["success"] is False
    assert response["error"]["code"] == "INVALID_REQUEST"