from edge_case_handler.edge_case_engine import evaluate
from edge_case_handler.sample_inputs import TESTS

print("=" * 60)
print("EDGE CASE HANDLING")
print("=" * 60)

for audio, text in TESTS:
    print(evaluate(audio, text))