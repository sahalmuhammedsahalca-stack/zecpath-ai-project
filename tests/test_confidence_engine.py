from confidence_analysis.confidence_engine import evaluate
from confidence_analysis.sample_responses import RESPONSES

print("=" * 60)
print("CONFIDENCE & STRESS ANALYSIS")
print("=" * 60)

for response in RESPONSES:
    print(evaluate(response))