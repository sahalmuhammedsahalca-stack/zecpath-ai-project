import re


def classify_sections(text):
    """
    Splits a resume into major sections based on headings.
    """

    headings = [
        "PROFESSIONAL SUMMARY",
        "PROFESSIONAL EXPERIENCE",
        "SKILLS",
        "EDUCATION",
        "PROJECTS",
        "CERTIFICATIONS"
    ]

    sections = {
        "summary": "",
        "experience": "",
        "skills": "",
        "education": "",
        "projects": "",
        "certifications": ""
    }

    current_section = None

    for line in text.split("\n"):
        line = line.strip()

        if line.upper() == "PROFESSIONAL SUMMARY":
            current_section = "summary"
            continue

        elif line.upper() == "PROFESSIONAL EXPERIENCE":
            current_section = "experience"
            continue

        elif line.upper() == "SKILLS":
            current_section = "skills"
            continue

        elif line.upper() == "EDUCATION":
            current_section = "education"
            continue

        elif line.upper() == "PROJECTS":
            current_section = "projects"
            continue

        elif line.upper() == "CERTIFICATIONS":
            current_section = "certifications"
            continue

        if current_section:
            sections[current_section] += line + "\n"

    return sections