from testing.sample_candidates import candidates
from testing.accuracy_metrics import calculate_accuracy
from testing.evaluation_metrics import evaluation_metrics
from testing.improvement_backlog import backlog

print("=" * 60)
print("ATS TESTING REPORT")
print("=" * 60)

print()

print("Candidate Categories Tested")

for candidate in candidates:
    print("-", candidate["role"])

print()

print("Accuracy")
print(calculate_accuracy(candidates), "%")

print()

print("Evaluation Metrics")
print(evaluation_metrics())

print()

print("Improvement Backlog")

for item in backlog:
    print("-", item)