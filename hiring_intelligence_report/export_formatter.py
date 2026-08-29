def format_report_for_export(report):
    """
    Convert the hiring intelligence report
    into an export-ready text format.
    """

    lines = []

    lines.append("HIRING INTELLIGENCE REPORT")
    lines.append("=" * 50)

    lines.append(f"Candidate ID: {report['candidate_id']}")
    lines.append(f"Candidate Name: {report['candidate_name']}")
    lines.append(f"Job Role: {report['job_role']}")

    lines.append("\nSCORE SUMMARY")
    lines.append("-" * 50)

    for area, score in report["scores"].items():
        lines.append(f"{area}: {score}")

    lines.append(
        f"Hiring Fit Percentage: "
        f"{report['hiring_fit_percentage']}"
    )

    lines.append("\nSTRENGTHS")
    lines.append("-" * 50)

    for strength in report["strengths"]:
        lines.append(f"- {strength}")

    lines.append("\nWEAKNESSES")
    lines.append("-" * 50)

    for weakness in report["weaknesses"]:
        lines.append(f"- {weakness}")

    lines.append("\nRISK INDICATORS")
    lines.append("-" * 50)

    for risk in report["risk_indicators"]:
        lines.append(f"- {risk}")

    lines.append("\nFINAL RECOMMENDATION")
    lines.append("-" * 50)
    lines.append(
        f"Recommendation: "
        f"{report['final_recommendation']}"
    )
    lines.append(
        f"Confidence Score: "
        f"{report['confidence_score']}"
    )

    lines.append("\nRECRUITER SUMMARY")
    lines.append("-" * 50)
    lines.append(report["recruiter_summary"])

    return "\n".join(lines)