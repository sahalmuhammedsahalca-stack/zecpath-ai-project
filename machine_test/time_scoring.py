def calculate_time_score(
    time_limit_minutes,
    time_taken_minutes
):
    """
    Calculate a time-based performance score.
    """

    if time_taken_minutes <= 0:
        return 100.0

    if time_taken_minutes <= time_limit_minutes:
        score = (
            time_limit_minutes
            - time_taken_minutes
        ) / time_limit_minutes * 100

        return round(min(100, 50 + score / 2), 2)

    overtime = (
        time_taken_minutes
        - time_limit_minutes
    )

    penalty = overtime * 5

    return round(max(0, 50 - penalty), 2)