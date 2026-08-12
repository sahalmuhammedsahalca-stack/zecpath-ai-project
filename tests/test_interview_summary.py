from interview_summary.report_generator import generate_report
from interview_summary.sample_candidate import CANDIDATE


print("=" * 60)
print("AI INTERVIEW SUMMARY")
print("=" * 60)

report = generate_report(CANDIDATE)

for key, value in report.items():
    print(f"{key}: {value}")