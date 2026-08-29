from optimization.cross_round_optimizer import (
    analyze_round_consistency
)


def run_test():
    print("CROSS-ROUND CONSISTENCY OPTIMIZATION")

    high = analyze_round_consistency(
        [85, 88, 90, 87]
    )

    moderate = analyze_round_consistency(
        [70, 80, 85]
    )

    low = analyze_round_consistency(
        [50, 75, 90]
    )

    print("\nHIGH CONSISTENCY")
    print(high)

    print("\nMODERATE CONSISTENCY")
    print(moderate)

    print("\nLOW CONSISTENCY")
    print(low)

    assert high["consistency"] == "High"
    assert moderate["consistency"] == "Moderate"
    assert low["consistency"] == "Low"

    print("\nINTEGRATION STATUS")
    print("Cross-Round Optimizer: PASSED")


if __name__ == "__main__":
    run_test()