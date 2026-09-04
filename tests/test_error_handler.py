from stabilization.error_handler import ErrorHandler


def test_value_error_response():
    handler = ErrorHandler()

    response = handler.handle(
        ValueError("Invalid score")
    )

    assert response["status"] == "error"
    assert response["error_type"] == "ValueError"
    assert "timestamp" in response


def test_permission_error_response():
    handler = ErrorHandler()

    response = handler.handle(
        PermissionError("Denied")
    )

    assert response["status"] == "error"
    assert response["error_type"] == "PermissionError"