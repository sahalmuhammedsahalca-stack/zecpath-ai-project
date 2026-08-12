"""
Future Async Jobs

Job 1
Resume Upload

↓

Job 2
Resume Parsing

↓

Job 3
ATS Scoring

↓

Job 4
Candidate Ranking

↓

Job 5
Shortlisting

Each job can run independently in the future
using Celery, RabbitMQ, Redis or FastAPI Background Tasks.
"""