from aptitude_logic.aptitude_engine import evaluate
from aptitude_logic.sample_candidate import ANSWER

print("=" * 60)
print("APTITUDE LOGIC ENGINE")
print("=" * 60)

result = evaluate(ANSWER)

for key, value in result.items():
    print(f"{key}: {value}")