def extract_entities(answer):

    text = answer.lower()

    return {
        "skills": [
            skill for skill in
            ["Python", "SQL", "Excel", "Power BI"]
            if skill.lower() in text
        ],
        "experience": "2 years" if "2 year" in text else "",
        "availability": "Immediate" if "immediate" in text else "",
        "salary": "5 LPA" if "5 lakh" in text else ""
    }