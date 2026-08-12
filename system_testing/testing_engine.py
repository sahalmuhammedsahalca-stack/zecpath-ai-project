from system_testing.screening_simulator import simulate
from system_testing.comparison_engine import compare
from system_testing.threshold_optimizer import optimize
from system_testing.rejection_handler import reduce_false_rejection

def evaluate(candidate):

    ai = simulate(candidate)
    diff = compare(ai, candidate["human_score"])

    status = optimize(ai)
    status = reduce_false_rejection(status, ai)

    return {
        "candidate": candidate["name"],
        "ai_score": ai,
        "human_score": candidate["human_score"],
        "difference": diff,
        "status": status
    }