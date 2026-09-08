from feature_polish.scoring_consistency import ScoringConsistency
from feature_polish.output_formatter import OutputFormatter
from feature_polish.report_clarity import ReportClarity
from feature_polish.error_handler import FeatureErrorHandler
from feature_polish.recruiter_output import RecruiterOutput
from feature_polish.feature_polish_controller import FeaturePolishController


def test_score_validation():
    scoring = ScoringConsistency()

    assert scoring.validate_score(90) is True
    assert scoring.normalize_score(90.456) == 90.46


def test_average_score():
    scoring = ScoringConsistency()

    result = scoring.calculate_average({
        "ATS": 92,
        "Screening": 90,
        "Technical": 88,
    })

    assert result == 90.0


def test_output_formatting():
    formatter = OutputFormatter()

    result = formatter.format_score(90)

    assert result == "90.00/100"


def test_report_section():
    report = ReportClarity()

    result = report.create_section(
        "Summary",
        "Candidate evaluation completed.",
    )

    assert result["title"] == "Summary"


def test_error_response():
    handler = FeatureErrorHandler()

    result = handler.create_error("missing_candidate")

    assert result["success"] is False
    assert result["error_type"] == "missing_candidate"


def test_recruiter_ranking():
    recruiter = RecruiterOutput()

    candidates = [
        {"candidate_id": "CAND001", "overall_score": 80},
        {"candidate_id": "CAND002", "overall_score": 95},
    ]

    result = recruiter.build_ranked_candidates(candidates)

    assert result[0]["candidate_id"] == "CAND002"


def test_feature_polish_controller():
    controller = FeaturePolishController()

    result = controller.process_candidate(
        candidate_id="CAND001",
        scores={
            "ATS": 92,
            "Screening": 90,
            "HR": 88,
            "Technical": 91,
        },
        recommendation="Highly Recommended",
    )

    assert result["success"] is True
    assert result["data"]["candidate"]["candidate_id"] == "CAND001"
    assert result["data"]["candidate"]["overall_score"] == 90.25


def test_missing_candidate_error():
    controller = FeaturePolishController()

    result = controller.process_candidate(
        candidate_id="",
        scores={"ATS": 90},
        recommendation="Review",
    )

    assert result["success"] is False
    assert result["error_type"] == "missing_candidate"