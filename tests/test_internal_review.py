from internal_review.system_walkthrough import SystemWalkthrough
from internal_review.review_report_generator import ReviewReportGenerator


def test_full_system_walkthrough():
    walkthrough = SystemWalkthrough()

    result = walkthrough.run_full_walkthrough()

    assert result["success"] is True
    assert result["stage_count"] == 5
    assert result["stages_reviewed"] == [
        "ATS",
        "Screening",
        "HR",
        "Technical",
        "Decision",
    ]


def test_walkthrough_summary():
    walkthrough = SystemWalkthrough()

    walkthrough.run_full_walkthrough()

    summary = walkthrough.get_summary()

    assert summary["complete"] is True
    assert summary["total_stages"] == 5
    assert summary["reviewed_stages"] == 5


def test_review_finding():
    generator = ReviewReportGenerator()

    finding = generator.create_finding(
        "accuracy",
        "Scoring consistency should be reviewed.",
        "Medium",
        "Run additional validation scenarios.",
    )

    assert finding["category"] == "accuracy"
    assert finding["priority"] == "Medium"


def test_review_summary():
    generator = ReviewReportGenerator()

    findings = [
        generator.create_finding(
            "accuracy",
            "Accuracy review",
            "High",
            "Validate scoring.",
        ),
        generator.create_finding(
            "ux",
            "UX review",
            "Medium",
            "Improve presentation.",
        ),
        generator.create_finding(
            "performance",
            "Performance review",
            "Low",
            "Continue benchmarking.",
        ),
    ]

    summary = generator.summarize(findings)

    assert summary["total_findings"] == 3
    assert summary["accuracy"] == 1
    assert summary["ux"] == 1
    assert summary["performance"] == 1
    assert summary["high_priority"] == 1
    assert summary["medium_priority"] == 1
    assert summary["low_priority"] == 1