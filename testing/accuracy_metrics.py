def calculate_accuracy(candidates):

    total_difference = 0

    for candidate in candidates:

        total_difference += abs(
            candidate["ats_score"] -
            candidate["manual_score"]
        )

    average_difference = total_difference / len(candidates)

    accuracy = 100 - average_difference

    return round(accuracy, 2)