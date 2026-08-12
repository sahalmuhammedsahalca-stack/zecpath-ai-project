from parsers.skill_dictionary import ALL_SKILLS


def extract_skills(text):
    """
    Extracts, normalizes, and removes duplicate skills.
    """

    found_skills = []

    text_lower = text.lower()

    for skill in ALL_SKILLS:
        if skill.lower() in text_lower:
            normalized_skill = skill.title()

            if normalized_skill not in found_skills:
                found_skills.append(normalized_skill)

    return found_skills