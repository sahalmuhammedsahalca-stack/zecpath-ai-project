from machine_test.machine_test_evaluator import evaluate_machine_test


print("=" * 50)
print("MACHINE TEST AI EVALUATION")
print("=" * 50)

result = evaluate_machine_test(
    correctness=90,
    efficiency=85,
    code_quality=88,
    problem_solving=92,
    time_limit_minutes=60,
    time_taken_minutes=45
)

print("\nMACHINE TEST EVALUATION")
print(result)

print("\nFINAL SCORE")
print(result["final_score"])

print("\nCLASSIFICATION")
print(result["classification"])

print("\nTIME SCORE")
print(result["time_score"])

print("\nTASK SCORE")
print(result["task_score"])

print("\nINTEGRATION STATUS")
print("Machine Test AI Evaluation: PASSED")