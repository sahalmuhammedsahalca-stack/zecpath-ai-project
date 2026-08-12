import re


def parse_resume(text):
    """
    Parses resume text and extracts structured information.
    """

    resume_data = {
        "name": "",
        "email": "",
        "phone": "",
        "skills": [],
        "education": [],
        "experience": []
    }

    lines = text.split("\n")

    # Extract Name
    for line in lines:
        line = line.strip()

        if line and line.isupper():
            resume_data["name"] = line.title()
            break

    # Extract Email
    email_match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if email_match:
        resume_data["email"] = email_match.group()

    # Extract Phone
    phone_match = re.search(
        r"(\+91[\s-]?\d{10}|\b\d{10}\b)",
        text
    )

    if phone_match:
        resume_data["phone"] = phone_match.group()

    # Extract Skills
    skills_list = [
        "SQL",
        "Python",
        "Power BI",
        "Microsoft Excel",
        "Google Sheets",
        "MySQL",
        "Pandas",
        "NumPy",
        "Data Cleaning",
        "Data Visualization",
        "Dashboard Development",
        "Business Intelligence",
        "EDA"
    ]

    extracted_skills = []

    for skill in skills_list:
        if re.search(re.escape(skill), text, re.IGNORECASE):
            extracted_skills.append(skill)

    resume_data["skills"] = extracted_skills

    # Extract Education
    education_keywords = [
        "Bachelor",
        "Master",
        "B.Tech",
        "M.Tech",
        "B.Sc",
        "M.Sc",
        "Diploma",
        "University",
        "College",
        "IGNOU"
    ]

    education_lines = []

    for line in lines:
        for keyword in education_keywords:
            if keyword.lower() in line.lower():
                education_lines.append(line.strip())
                break

    resume_data["education"] = education_lines

    # Extract Experience
    experience_lines = []
    capture = False

    for line in lines:
        if "PROFESSIONAL EXPERIENCE" in line.upper():
            capture = True
            continue

        if capture:
            if "SKILLS" in line.upper():
                break

            if line.strip():
                experience_lines.append(line.strip())

    resume_data["experience"] = experience_lines

    return resume_data