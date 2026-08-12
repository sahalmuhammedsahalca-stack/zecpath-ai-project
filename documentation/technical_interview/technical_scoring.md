# Technical Interview AI – Technical Skill Scoring Documentation

## 1. Overview

The Technical Skill Scoring module evaluates a candidate's technical performance during the technical interview.

The scoring system considers multiple technical evaluation parameters and produces an explainable technical score.

The module also considers question type and question difficulty when generating a normalized technical evaluation.

---

## 2. Purpose

The Technical Skill Scoring module is responsible for:

- Evaluating technical answer quality
- Calculating technical scores
- Measuring technical depth
- Applying question-type weighting
- Applying difficulty-level weighting
- Generating explainable technical evaluations
- Generating structured technical evaluation reports

---

## 3. Evaluation Parameters

The technical score is calculated using four main parameters:

| Parameter | Description |
|---|---|
| Accuracy | Measures correctness of the candidate's answer |
| Depth | Measures depth of technical understanding |
| Logical Reasoning | Measures the candidate's reasoning ability |
| Real-World Applicability | Measures practical application of technical knowledge |

The four parameters are combined to calculate the base technical score.

---

## 4. Technical Score Calculation

The base technical score is calculated as the average of:

- Accuracy
- Depth
- Logical Reasoning
- Real-World Applicability

The resulting score is rounded to two decimal places.

Example:

Accuracy = 90

Depth = 88

Logical Reasoning = 92

Real-World Applicability = 90

The resulting technical score is:

90.0

---

## 5. Technical Depth Classification

The system classifies technical understanding according to the calculated score.

| Score | Classification |
|---|---|
| 80 and above | Deep Technical Understanding |
| 60–79.99 | Moderate Technical Understanding |
| Below 60 | Shallow Technical Understanding |

This classification provides an easy-to-understand interpretation of the candidate's technical performance.

---

## 6. Question Type Weighting

Different technical question types may have different importance during evaluation.

The system uses the following weights:

| Question Type | Weight |
|---|---:|
| Conceptual | 1.00 |
| Coding | 1.05 |
| Practical | 1.05 |
| Debugging | 1.10 |
| Scenario-Based | 1.10 |
| Architecture | 1.15 |
| System Design | 1.20 |

The weighting allows more complex or practical question categories to have greater influence on the final technical evaluation.

---

## 7. Difficulty-Level Normalization

The system also considers the difficulty level of the technical question.

| Difficulty Level | Weight |
|---|---:|
| Level 1 – Basic | 1.00 |
| Level 2 – Intermediate | 1.00 |
| Level 3 – Advanced | 1.05 |
| Level 4 – Scenario-Based | 1.10 |
| Level 5 – System Design | 1.15 |

Higher-level technical questions can therefore contribute more strongly to the normalized technical score.

The final normalized score is limited to a maximum of 100.

---

## 8. Technical Question Score

The system first calculates the base technical score.

The question-type weight is then applied.

The resulting score is normalized according to the question difficulty.

This produces the final technical question score.

---

## 9. Explainable Technical Evaluation

The system generates an evaluation containing:

- Accuracy
- Depth
- Logical Reasoning
- Real-World Applicability
- Technical Score
- Technical Depth
- Explanation

The explanation states that the technical score is based on the four evaluation parameters.

This supports explainable candidate evaluation.

---

## 10. Technical Evaluation Report

The module can generate a structured technical evaluation report containing:

- Candidate name
- Question type
- Difficulty level
- Technical score
- Technical depth
- Skill breakdown
- Evaluation explanation

This structured output can be used by other recruitment modules.

---

## 11. Example Evaluation

Example input:

```text
Candidate: Sahal

Accuracy: 90
Depth: 88
Logical Reasoning: 92
Real-World Applicability: 90