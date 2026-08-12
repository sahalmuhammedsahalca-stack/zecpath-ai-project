"""
Simulates connection with ATS output.

Later this module can be replaced by:
- Database
- API
- Resume Parser
"""

candidate = {
    "candidate_name": "Muhammed Sahal",
    "job_role": "Data Analyst",
    "ats_score": 88.82,
    "experience": 2,
    "location": "Kochi",
    "skills": [
        "Python",
        "SQL",
        "Power BI",
        "Excel"
    ]
}


def get_candidate():

    return candidate