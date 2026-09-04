# Request and Response Schema Definitions

## Standard Request Structure

### Resume Parsing

```json
{
    "candidate_id": "CAND001",
    "resume_path": "resume.pdf"
}
{
    "candidate_id": "CAND001",
    "resume_data": {},
    "job_description": {}
}
{
    "candidate_id": "CAND001",
    "resume_score": 85,
    "screening_questions": []
}
{
    "candidate_id": "CAND001",
    "interview_id": "INT001",
    "responses": []
}
{
    "candidate_id": "CAND001",
    "ats_score": 85,
    "screening_score": 80,
    "interview_score": 88
}
{
    "success": true,
    "request_id": "REQ001",
    "data": {},
    "error": null
}
{
    "success": false,
    "request_id": "REQ001",
    "data": null,
    "error": {
        "code": "INVALID_REQUEST",
        "message": "Invalid payload"
    }
}