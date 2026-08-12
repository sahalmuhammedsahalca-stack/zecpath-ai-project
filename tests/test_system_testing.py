from system_testing.testing_engine import evaluate
from system_testing.sample_candidates import CANDIDATES

print("=" * 60)
print("SYSTEM TESTING")
print("=" * 60)

for candidate in CANDIDATES:
    print(evaluate(candidate))