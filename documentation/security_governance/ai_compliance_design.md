# AI Compliance Design

## 1. Overview

The Zecpath AI system requires governance controls to support responsible,
auditable, and controlled use of AI-assisted recruitment decisions.

The Day 55 compliance design focuses on:

- Auditability
- Data retention
- Consent-based data usage
- Controlled storage
- Role-based access

## 2. Auditability

The system records two major categories of audit events:

### Score Logs

Score logs record:

- Candidate ID
- Interview round
- Score
- Scoring source
- Timestamp

### Decision Logs

Decision logs record:

- Candidate ID
- Final decision
- Confidence score
- Decision source
- Timestamp

## 3. Data Retention

Retention periods are defined for different categories of data.

| Data Type | Default Retention |
|---|---:|
| Audit logs | 365 days |
| Transcripts | 180 days |
| Reports | 365 days |

The retention module determines whether stored information has reached
its configured retention period.

## 4. Consent

Candidate data processing requires recorded consent for the intended purpose.

Supported purposes include:

- Recruitment evaluation
- Interview analysis
- Report generation
- Audit

Consent can also be revoked.

## 5. Secure Storage

Sensitive transcripts and reports are assigned controlled storage locations.

The storage layer also validates filenames and prevents unsafe path traversal.

Actual encryption at rest is considered a deployment/storage-layer
requirement and is not falsely represented as implemented by the current
local storage module.

## 6. Access Control

Role-based permissions restrict access to governance data.

Supported roles include:

- Admin
- Recruiter
- Analyst
- Auditor

## 7. Compliance Principle

The governance layer provides traceability, controlled processing,
limited retention, consent checks, and restricted access for AI-assisted
recruitment workflows.