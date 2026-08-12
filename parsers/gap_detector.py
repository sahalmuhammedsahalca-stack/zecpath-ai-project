import re


def detect_gap(experience_data):
    """
    Detects employment gaps between jobs.
    """

    months = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }

    gaps = []

    for i in range(len(experience_data) - 1):

        current = experience_data[i]["duration"]
        nxt = experience_data[i + 1]["duration"]

        current_match = re.match(
            r"([A-Za-z]{3}) (\d{4})\s*–\s*([A-Za-z]{3}) (\d{4})",
            current
        )

        next_match = re.match(
            r"([A-Za-z]{3}) (\d{4})\s*–\s*([A-Za-z]{3}) (\d{4})",
            nxt
        )

        if current_match and next_match:

            _, _, end_month, end_year = current_match.groups()
            start_month, start_year, _, _ = next_match.groups()

            end = int(end_year) * 12 + months[end_month]
            start = int(start_year) * 12 + months[start_month]

            gap = start - end

            gaps.append(gap)

    return gaps