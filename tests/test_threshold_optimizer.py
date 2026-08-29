from optimization.threshold_optimizer import (
    evaluate_thresholds,
    compare_thresholds
)


def run_test():
    print("SCORING THRESHOLD OPTIMIZATION")

    high = evaluate_thresholds(90)
    recommended = evaluate_thresholds(75)
    review = evaluate_thresholds(65)
    low = evaluate_thresholds(50)

    print("\nHIGH SCORE")
    print(high)

    print("\nRECOMMENDED SCORE")
    print(recommended)

    print("\nREVIEW SCORE")
    print(review)

    print("\nLOW SCORE")
    print(low)

    comparison = compare_thresholds(82)

    print("\nTHRESHOLD COMPARISON")
    print(comparison)

    assert high == "Highly Recommended"
    assert recommended == "Recommended"
    assert review == "Needs Review"
    assert low == "Not Recommended"

    print("\nINTEGRATION STATUS")
    print("Threshold Optimizer: PASSED")


if __name__ == "__main__":
    run_test()