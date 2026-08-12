from hr_interview_simulation.interview_simulator import simulate_interview
from hr_interview_simulation.manual_evaluation import evaluate_manually
from hr_interview_simulation.comparison_engine import compare
from hr_interview_simulation.inconsistency_detector import detect_inconsistency


def run_simulation(candidates):

    results = []

    for candidate in candidates:

        ai = simulate_interview(candidate)
        manual = evaluate_manually(candidate)

        comparison = compare(
            ai["ai_score"],
            manual["manual_score"]
        )

        result = {
            "candidate": candidate["name"],
            "type": candidate["type"],
            "ai_score": ai["ai_score"],
            "manual_score": manual["manual_score"],
            "difference": comparison["difference"],
            "status": comparison["status"],
            "evaluation": detect_inconsistency(
                comparison["difference"]
            )
        }

        results.append(result)

    return results