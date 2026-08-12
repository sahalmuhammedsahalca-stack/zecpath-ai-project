COMMON_SKILLS = {

    "python": "Python",

    "sql": "SQL",

    "mysql": "MySQL",

    "power bi": "Power BI",

    "excel": "Excel",

    "pandas": "Pandas",

    "numpy": "NumPy"

}


def normalize_skill(skill):

    return COMMON_SKILLS.get(

        skill.lower(),

        skill

    )