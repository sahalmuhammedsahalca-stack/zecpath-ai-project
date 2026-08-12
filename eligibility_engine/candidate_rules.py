"""
Recruiter configurable rules
"""

JOB_RULES = {
    "Data Analyst": {
        "minimum_score": 80,
        "minimum_experience": 1,
        "mandatory_skills": [
            "Python",
            "SQL",
            "Power BI"
        ],
        "locations": [
            "Kochi",
            "Bangalore",
            "Remote"
        ]
    },

    "Python Developer": {
        "minimum_score": 85,
        "minimum_experience": 2,
        "mandatory_skills": [
            "Python",
            "Django"
        ],
        "locations": [
            "Remote",
            "Chennai"
        ]
    }
}