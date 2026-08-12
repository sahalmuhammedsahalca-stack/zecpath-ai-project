from communication_analysis.behavior_engine import analyze_behavior
from communication_analysis.sample_responses import RESPONSES

print("=" * 60)
print("COMMUNICATION ANALYSIS")
print("=" * 60)

for response in RESPONSES:
    print(analyze_behavior(response))