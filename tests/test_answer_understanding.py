from answer_understanding.answer_engine import analyze_answer
from answer_understanding.sample_answers import ANSWERS

print("=" * 60)
print("ANSWER UNDERSTANDING ENGINE")
print("=" * 60)

for answer in ANSWERS:
    print(analyze_answer(answer))