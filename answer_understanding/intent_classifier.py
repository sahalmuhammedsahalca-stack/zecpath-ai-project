def classify_intent(answer):

    text = answer.lower()

    if any(word in text for word in ["python", "sql", "excel", "power bi"]):
        return "Skills"

    elif "year" in text or "experience" in text:
        return "Experience"

    elif "notice" in text or "available" in text:
        return "Availability"

    elif "salary" in text or "lakh" in text:
        return "Salary"

    return "General"