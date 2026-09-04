class APIOutputValidator:
    """
    Validates structured outputs before they are returned
    by AI modules or APIs.
    """

    REQUIRED_FIELDS = {
        "status",
    }

    VALID_STATUSES = {
        "success",
        "error",
    }

    def validate(self, response):
        if not isinstance(response, dict):
            raise ValueError(
                "API response must be a dictionary"
            )

        missing_fields = [
            field
            for field in self.REQUIRED_FIELDS
            if field not in response
        ]

        if missing_fields:
            raise ValueError(
                f"Missing response fields: {missing_fields}"
            )

        if response["status"] not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid response status: "
                f"{response['status']}"
            )

        return True

    def success_response(self, data=None):
        response = {
            "status": "success",
            "data": data if data is not None else {},
        }

        self.validate(response)

        return response

    def error_response(self, message):
        response = {
            "status": "error",
            "message": message,
        }

        self.validate(response)

        return response