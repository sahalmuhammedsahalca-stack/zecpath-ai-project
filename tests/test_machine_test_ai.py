from machine_test.task_manager import (
    create_machine_test,
    validate_task_type
)

from machine_test.task_evaluator import (
    evaluate_task
)

from machine_test.scoring_engine import (
    calculate_machine_test_score,
    classify_machine_test_score
)

from machine_test.time_scoring import (
    calculate_time_score
)


print("=" * 50)
print("MACHINE TEST AI")
print("=" * 50)


print("\nTASK CREATION")

test = create_machine_test(
    role="Python Developer",
    task_type="coding",
    difficulty="Intermediate",
    required_skills=[
        "Python",
        "Problem Solving",
        "Debugging"
    ],
    time_limit=30
)

print(test)


print("\nTASK TYPE VALIDATION")

print(
    validate_task_type("coding")
)

print(
    validate_task_type("unknown")
)


print("\nTASK EVALUATION")

evaluation = evaluate_task(
    correctness=90,
    efficiency=85,
    code_quality=88,
    problem_solving=92
)

print(evaluation)


print("\nTIME SCORING")

time_score = calculate_time_score(
    time_limit_minutes=30,
    time_taken_minutes=24
)

print("TIME SCORE")
print(time_score)


print("\nFINAL MACHINE TEST SCORE")

final_score = calculate_machine_test_score(
    correctness=90,
    efficiency=85,
    code_quality=88,
    problem_solving=92,
    time_score=time_score
)

print("FINAL SCORE")
print(final_score)

print("\nCLASSIFICATION")

print(
    classify_machine_test_score(final_score)
)