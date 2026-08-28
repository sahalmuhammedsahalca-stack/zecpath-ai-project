from final_recommendation.decision_engine import (
    generate_final_decision
)


def run_test():
    print("FINAL RECOMMENDATION AI")

    selected = generate_final_decision(
        "CAND001",
        "Test Candidate",
        88,
        85,
        10
    )

    print("\nSELECTED CASE")
    print(selected)

    hold = generate_final_decision(
        "CAND002",
        "Review Candidate",
        68,
        70,
        20
    )

    print("\nHOLD / REVIEW CASE")
    print(hold)

    rejected = generate_final_decision(
        "CAND003",
        "Risk Candidate",
        75,
        65,
        90
    )

    print("\nREJECTED CASE")
    print(rejected)

    assert selected["recommendation"] == "Selected"
    assert hold["recommendation"] == "Hold / Review"
    assert rejected["recommendation"] == "Rejected"

    print("\nINTEGRATION STATUS")
    print("Final Recommendation AI: PASSED")


if __name__ == "__main__":
    run_test()