# HR Interview AI – Architecture Document

## 1. Overview

The HR Interview AI is an AI-assisted recruitment system designed to evaluate candidates through multiple stages of the hiring process.

The system combines resume analysis, screening, communication assessment, HR interview evaluation, scoring, ranking, and compliance checks.

## 2. Main System Components

### Resume & ATS Processing
- Resume parsing
- Job description parsing
- Skill extraction
- ATS scoring
- Candidate eligibility

### Screening System
- Screening question evaluation
- Answer understanding
- Screening scoring
- Candidate ranking

### Communication Analysis
- Speech processing
- Communication evaluation
- Communication scoring
- Confidence analysis

### HR Interview System
- Interview question generation
- Conversation flow
- Dynamic follow-up questions
- HR interview simulation
- Interview summary

### Scoring System
- Unified scoring
- Candidate ranking
- Performance optimization
- False-result handling

### Compliance
- Consent management
- Fairness review
- Bias checking
- Explainability
- Data retention

## 3. High-Level Data Flow

Candidate
↓
Resume Upload
↓
Resume Parser
↓
ATS Evaluation
↓
Candidate Eligibility
↓
AI Screening
↓
Communication Analysis
↓
HR Interview
↓
Interview Evaluation
↓
Unified Scoring
↓
Candidate Ranking
↓
Final Hiring Evaluation

## 4. Important Project Modules

| Module | Responsibility |
|---|---|
| parsers | Extract structured information from resumes and job descriptions |
| ats_engine | Perform ATS-related candidate evaluation |
| screening_ai | Support AI screening |
| screening_scoring | Calculate screening scores |
| communication_analysis | Analyze communication-related signals |
| communication_scoring | Calculate communication scores |
| confidence_analysis | Analyze confidence-related signals |
| interview_question_engine | Generate interview questions |
| conversation_flow | Manage interview conversation flow |
| dynamic_followup | Handle adaptive follow-up questions |
| hr_interview_engine | Manage HR interview processing |
| hr_interview_simulation | Simulate and evaluate HR interviews |
| unified_scoring | Combine evaluation scores |
| candidate_ranking | Rank candidates |
| optimization | Improve processing and scoring behavior |
| ethics_compliance | Handle ethical and compliance checks |

## 5. Testing Architecture

The project contains dedicated test modules for validating individual components and system-level behavior.

Testing includes:

- Unit-level component testing
- Scoring validation
- System testing
- Edge-case testing
- API testing
- Ethics and compliance testing
- Optimization testing

## 6. Design Principles

The system is designed around:

- Modular architecture
- Reusable components
- Independent testing
- Explainable scoring
- Fair candidate evaluation
- Data protection
- Maintainability
- Integration readiness

## 7. Maintenance

Each major AI component is separated into its own module so that developers can modify or improve one component without unnecessarily changing the entire system.

Testing modules should be executed after significant changes to ensure existing functionality continues to work.