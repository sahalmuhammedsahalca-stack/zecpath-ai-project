from hiring_intelligence_report.candidate_profile import (
    generate_candidate_profile
)

from hiring_intelligence_report.export_formatter import (
    format_report_for_export
)


def run_test():

    print("=" * 50)
    print("HIRING INTELLIGENCE REPORT GENERATOR")
    print("=" * 50)

    report = generate_candidate_profile(
        "CAND001",
        "Muhammed Sahal",
        "Data Analyst",
        88,
        90,
        90,
        88,
        85,
        10,
        89.75,
        "Selected",
        87.67
    )

    print("\nFULL CANDIDATE AI PROFILE")
    print(report)

    print("\nEXPORT-READY REPORT")
    print("=" * 50)

    export_report = format_report_for_export(report)

    print(export_report)

    assert report["candidate_id"] == "CAND001"
    assert report["final_recommendation"] == "Selected"
    assert report["profile_status"] == "Complete"
    assert report["hiring_fit_percentage"] == 89.75

    print("\nINTEGRATION STATUS")
    print("Hiring Intelligence Report: PASSED")


if __name__ == "__main__":
    run_test()