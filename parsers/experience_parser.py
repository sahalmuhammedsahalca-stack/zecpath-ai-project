import re


def parse_experience(text):
    """
    Extracts structured work experience
    from resume text.
    """

    experience = []

    pattern = re.findall(
        r"([A-Za-z &()]+)\n"
        r"([A-Za-z0-9 .,&\-–]+)\n"
        r"([A-Za-z]{3} \d{4} – [A-Za-z]{3} \d{4})",
        text
    )

    for job_title, company, duration in pattern:

        experience.append({
            "job_title": job_title.strip(),
            "company": company.strip(),
            "duration": duration.strip()
        })

    return experience