from optimization.false_decision_analyzer import analyze_decision


def run_test():
    print("FALSE POSITIVE / FALSE NEGATIVE ANALYSIS")

    correct = analyze_decision(
        "Selected",
        "Selected"
    )

    print("\nCORRECT DECISION")
    print(correct)

    false_positive = analyze_decision(
        "Selected",
        "Rejected"
    )

    print("\nFALSE POSITIVE")
    print(false_positive)

    false_negative = analyze_decision(
        "Rejected",
        "Selected"
    )

    print("\nFALSE NEGATIVE")
    print(false_negative)

    assert correct["decision_status"] == "Correct"
    assert false_positive["error_type"] == "False Positive"
    assert false_negative["error_type"] == "False Negative"

    print("\nINTEGRATION STATUS")
    print("False Decision Analyzer: PASSED")


if __name__ == "__main__":
    run_test()