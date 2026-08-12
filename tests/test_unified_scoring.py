from unified_scoring.unified_score import generate_unified_score


print("=" * 60)
print("UNIFIED SCORING ENGINE")
print("=" * 60)


candidate = generate_unified_score(
    candidate_name="Muhammed Sahal",
    job_role="Data Analyst",
    ats_score=88.82,
    screening_score=90.67,
    hr_interview_score=90
)


for key, value in candidate.items():
    print(f"{key}: {value}")


print("=" * 60)