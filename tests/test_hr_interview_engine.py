from hr_interview_engine.hr_interview_engine import start_interview
from hr_interview_engine.sample_candidate import CANDIDATE

print("=" * 60)
print("HR INTERVIEW ENGINE")
print("=" * 60)

result = start_interview(
    CANDIDATE["level"],
    CANDIDATE["role_type"]
)

print(result)