from machine_test.task_evaluator import evaluate_task
from machine_test.time_scoring import calculate_time_score
from machine_test.scoring_engine import (
    calculate_machine_test_score,
    classify_machine_test_score
)


def evaluate_machine_test(
    correctness,
    efficiency,
    code_quality,
    problem_solving,
    time_limit_minutes,
    time_taken_minutes
):
    """
    Evaluate overall candidate performance in a machine test.
    """

    task_evaluation = evaluate_task(
        correctness,
        efficiency,
        code_quality,
        problem_solving
    )

    time_score = calculate_time_score(
        time_limit_minutes,
        time_taken_minutes
    )

    final_score = calculate_machine_test_score(
        correctness,
        efficiency,
        code_quality,
        problem_solving,
        time_score
    )

    classification = classify_machine_test_score(
        final_score
    )

    return {
        "correctness": correctness,
        "efficiency": efficiency,
        "code_quality": code_quality,
        "problem_solving": problem_solving,
        "time_limit_minutes": time_limit_minutes,
        "time_taken_minutes": time_taken_minutes,
        "task_score": task_evaluation["task_score"],
        "time_score": time_score,
        "final_score": final_score,
        "classification": classification,
        "explanation": (
            "Machine test evaluation is based on correctness, "
            "efficiency, code quality, problem-solving, "
            "and time performance."
        )
    }