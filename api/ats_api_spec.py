"""
ATS API Specification

1. Resume Upload API

POST /api/upload_resume

Request:
{
    "file": "resume.pdf"
}

Response:
{
    "message": "Resume uploaded successfully"
}


-------------------------------------


2. Resume Parsing API

POST /api/parse_resume

Response:
{
    "name": "...",
    "skills": [...],
    "education": [...],
    "experience": [...]
}


-------------------------------------


3. ATS Scoring API

POST /api/score_resume

Response:
{
    "final_score": 88.82
}


-------------------------------------


4. Candidate Ranking API

POST /api/rank_candidates

Response:
{
    "ranked_candidates":[]
}


-------------------------------------


5. Shortlisting API

POST /api/shortlist

Response:
{
    "status":"Shortlisted"
}
"""