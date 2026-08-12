import re


def parse_job_description(text):
    """
    Parses a job description and extracts
    structured information.
    """

    job_data = {
        "job_title": "",
        "skills": [],
        "experience": "",
        "education": ""
    }

    # Extract Job Title
    match = re.search(r"Job Title:\s*(.*)", text)
    if match:
        job_data["job_title"] = match.group(1).strip()

    # Extract Required Skills
    skills_match = re.search(
        r"Required Skills:\s*(.*?)\n\s*Responsibilities:",
        text,
        re.DOTALL
    )

    if skills_match:
        skills_text = skills_match.group(1)
        skills = []

        for line in skills_text.split("\n"):
            line = line.replace("-", "").strip()
            if line:
                skills.append(line)

        job_data["skills"] = skills

    # Extract Experience Required
    experience_match = re.search(
        r"Experience Required:\s*(.*?)\n\s*Education:",
        text,
        re.DOTALL
    )

    if experience_match:
        job_data["experience"] = experience_match.group(1).strip()

    # Extract Education
    education_match = re.search(
        r"Education:\s*(.*?)\n\s*Required Skills:",
        text,
        re.DOTALL
    )

    if education_match:
        job_data["education"] = education_match.group(1).strip()

    return job_data