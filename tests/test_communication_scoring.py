from communication_scoring.communication_engine import evaluate
from communication_scoring.sample_scores import SAMPLES

print("=" * 60)
print("COMMUNICATION SCORING")
print("=" * 60)

for sample in SAMPLES:

    result = evaluate(*sample)

    print(result)