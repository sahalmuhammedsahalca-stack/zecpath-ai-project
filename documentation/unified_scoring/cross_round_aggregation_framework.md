# Cross-Round Aggregation Framework

## 1. Purpose

The Cross-Round Aggregation Framework combines evaluation results from multiple recruitment stages into one unified hiring intelligence score.

The framework provides a structured method for combining ATS, Screening, HR Interview, Technical Interview, and Machine Test results.

## 2. Evaluation Rounds

The system aggregates the following stages:

- ATS
- Screening
- HR Interview
- Technical Interview
- Machine Test

## 3. Processing Pipeline

The aggregation pipeline follows:

Round Score Collection
↓
Score Validation
↓
Score Normalization
↓
Role Weight Selection
↓
Weighted Score Calculation
↓
Hiring Fit Score
↓
Candidate Classification
↓
Unified Candidate Score Object

## 4. Score Collection

Each candidate receives scores from the completed recruitment stages.

Each score is represented on a 0-100 scale.

## 5. Score Normalization

Scores are normalized to ensure that all evaluation rounds use a consistent 0-100 scale.

This prevents invalid values from affecting the final evaluation.

## 6. Role-Based Weighting

Different job roles may require different evaluation priorities.

For example, a Python Developer may receive higher weighting for Technical Interview and Machine Test performance.

## 7. Weighted Aggregation

Each normalized round score is multiplied by its assigned role-specific weight.

The weighted scores are then combined to produce the final Hiring Fit Score.

## 8. Hiring Fit Score

The Hiring Fit Score represents the candidate's overall performance across the recruitment process.

The score is represented as a percentage from 0 to 100.

## 9. Classification

The final score is classified as:

- 85-100: Excellent Hiring Fit
- 75-84: Strong Hiring Fit
- 60-74: Moderate Hiring Fit
- Below 60: Low Hiring Fit

## 10. Unified Candidate Score Object

The system stores:

- Candidate ID
- Candidate name
- Role
- Original round scores
- Normalized scores
- Role weights
- Weighted scores
- Hiring Fit Score
- Classification
- Explanation

## 11. Transparency

The aggregation engine retains the individual scores and weights used in the calculation.

This allows reviewers to understand exactly how the final Hiring Fit Score was produced.

## 12. Expected Outcome

The Cross-Round Aggregation Framework provides a modular and explainable method for combining recruitment evaluation stages into a unified candidate assessment.