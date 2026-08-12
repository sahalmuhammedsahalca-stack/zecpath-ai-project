from communication_evaluation.communication_engine import evaluate
from communication_evaluation.sample_answers import ANSWERS

print("=" * 60)
print("COMMUNICATION SKILL EVALUATION")
print("=" * 60)

for answer in ANSWERS:
    print(evaluate(answer))