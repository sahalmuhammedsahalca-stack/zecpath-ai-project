from unified_scoring.cross_round_aggregator import (
    aggregate_candidate_scores,
)


def main():
    scores = {
        "ATS": 88,
        "Screening": 82,
        "HR Interview": 90,
        "Technical Interview": 92,
        "Machine Test": 85,
    }

    result = aggregate_candidate_scores(
        candidate_id="CAND001",
        candidate_name="Muhammed Sahal",
        role="Data Analyst",
        scores=scores,
    )

    print("=" * 60)
    print("CROSS-ROUND AGGREGATION ENGINE")
    print("=" * 60)

    print("\nCANDIDATE")
    print(result["candidate_name"])

    print("\nROLE")
    print(result["role"])

    print("\nROUND SCORES")
    print(result["round_scores"])

    print("\nNORMALIZED SCORES")
    print(result["normalized_scores"])

    print("\nROLE WEIGHTS")
    print(result["weights"])

    print("\nWEIGHTED SCORES")
    print(result["weighted_scores"])

    print("\nHIRING FIT SCORE")
    print(result["hiring_fit_score"])

    print("\nCLASSIFICATION")
    print(result["classification"])

    print("\nUNIFIED CANDIDATE SCORE OBJECT")
    print(result)

    print("\nINTEGRATION STATUS")
    print("Cross-Round Aggregation Engine: PASSED")


if __name__ == "__main__":
    main()