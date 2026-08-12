from dynamic_followup.followup_engine import evaluate
from dynamic_followup.sample_answers import SAMPLES

print("=" * 60)
print("DYNAMIC FOLLOW-UP ENGINE")
print("=" * 60)

for answer, confidence in SAMPLES:
    print(evaluate(answer, confidence))