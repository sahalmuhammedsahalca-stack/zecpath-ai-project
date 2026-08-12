import re


def calculate_total_experience(experience_data):
    """
    Calculates total experience in months.
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

    total_months = 0

    for job in experience_data:

        duration = job["duration"]

        match = re.match(
            r"([A-Za-z]{3}) (\d{4})\s*–\s*([A-Za-z]{3}) (\d{4})",
            duration
        )

        if match:

            start_month, start_year, end_month, end_year = match.groups()

            start = int(start_year) * 12 + months[start_month]
            end = int(end_year) * 12 + months[end_month]

            total_months += (end - start)

    years = total_months // 12
    remaining_months = total_months % 12

    return {
        "total_months": total_months,
        "experience": f"{years} Years {remaining_months} Months"
    }