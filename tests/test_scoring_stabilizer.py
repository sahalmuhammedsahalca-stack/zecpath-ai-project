from stabilization.scoring_stabilizer import ScoringStabilizer


def test_score_normalization():
    stabilizer = ScoringStabilizer()

    assert stabilizer.normalize_score(85.678) == 85.68


def test_score_upper_boundary():
    stabilizer = ScoringStabilizer()

    assert stabilizer.normalize_score(120) == 100


def test_score_lower_boundary():
    stabilizer = ScoringStabilizer()

    assert stabilizer.normalize_score(-10) == 0


def test_average_score():
    stabilizer = ScoringStabilizer()

    assert stabilizer.calculate_average(
        [80, 90, 100]
    ) == 90


def test_score_consistency():
    stabilizer = ScoringStabilizer()

    result = stabilizer.check_consistency(
        [80, 85, 90]
    )

    assert result["consistent"] is True