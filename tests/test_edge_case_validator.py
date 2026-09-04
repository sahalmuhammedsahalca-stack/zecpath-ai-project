from stabilization.edge_case_validator import (
    EdgeCaseValidator,
)


def test_valid_candidate_id():
    validator = EdgeCaseValidator()

    assert validator.validate_candidate_id(
        "CAND001"
    ) is True


def test_empty_candidate_id():
    validator = EdgeCaseValidator()

    assert validator.validate_candidate_id(
        ""
    ) is False


def test_valid_score():
    validator = EdgeCaseValidator()

    assert validator.validate_score(85) is True


def test_invalid_score():
    validator = EdgeCaseValidator()

    assert validator.validate_score(150) is False


def test_empty_text():
    validator = EdgeCaseValidator()

    assert validator.validate_text("") is False


def test_valid_list():
    validator = EdgeCaseValidator()

    assert validator.validate_list(
        ["question"]
    ) is True