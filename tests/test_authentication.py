import pytest

from api_integration.authentication import APIAuthentication


def test_valid_authentication_method():

    assert APIAuthentication.validate_method("BEARER_TOKEN")


def test_invalid_authentication_method():

    with pytest.raises(ValueError):
        APIAuthentication.validate_method("PASSWORD")


def test_security_policy():

    policy = APIAuthentication.create_security_policy()

    assert policy["authentication_required"] is True
    assert policy["encryption_in_transit"] is True
    assert policy["least_privilege"] is True