from api_integration.error_retry import (
    RetryPolicy,
    APIErrorHandler,
)


def test_retryable_error():

    assert RetryPolicy.should_retry(
        "TIMEOUT",
        1,
        3,
    )


def test_non_retryable_error():

    assert not RetryPolicy.should_retry(
        "INVALID_REQUEST",
        1,
        3,
    )


def test_retry_limit():

    assert not RetryPolicy.should_retry(
        "TIMEOUT",
        3,
        3,
    )


def test_error_response():

    response = APIErrorHandler.create_error(
        "TIMEOUT",
        "Request timed out",
        True,
    )

    assert response["success"] is False
    assert response["error"]["retryable"] is True