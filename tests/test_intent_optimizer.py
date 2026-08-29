from optimization.intent_optimizer import (
    normalize_intent,
    analyze_intent_consistency
)


def run_test():
    print("INTENT DETECTION OPTIMIZATION")

    technical = normalize_intent("coding")
    behavioral = normalize_intent("behavioral question")
    hr = normalize_intent("HR")
    unknown = normalize_intent("something else")

    print("\nNORMALIZED INTENTS")
    print(technical)
    print(behavioral)
    print(hr)
    print(unknown)

    consistency = analyze_intent_consistency(
        ["technical", "coding", "technical question"]
    )

    print("\nINTENT CONSISTENCY")
    print(consistency)

    assert technical == "Technical"
    assert behavioral == "Behavioral"
    assert hr == "HR"
    assert unknown == "Unknown"
    assert consistency["consistency"] == "High"

    print("\nINTEGRATION STATUS")
    print("Intent Optimizer: PASSED")


if __name__ == "__main__":
    run_test()