from interview_question_engine.interview_engine import generate_interview
from interview_question_engine.sample_candidates import CANDIDATE

print("=" * 60)
print("AI INTERVIEW QUESTION ENGINE")
print("=" * 60)

print(generate_interview(CANDIDATE["role"]))