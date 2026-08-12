def format_result(result):

    print("=" * 60)
    print("CANDIDATE ELIGIBILITY RESULT")
    print("=" * 60)

    for key, value in result.items():
        print(f"{key}: {value}")

    print("=" * 60)