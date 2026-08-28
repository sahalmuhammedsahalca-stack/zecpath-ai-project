# Hiring Fit Scoring Model

## 1. Purpose

The Hiring Fit Scoring Model converts multiple recruitment stage scores into one final Hiring Fit Score.

## 2. Evaluation Parameters

The model uses:

- ATS Score
- Screening Score
- HR Interview Score
- Technical Interview Score
- Machine Test Score

## 3. Default Weighting

The default weighting is:

| Evaluation Round | Weight |
|---|---:|
| ATS | 20% |
| Screening | 15% |
| HR Interview | 15% |
| Technical Interview | 25% |
| Machine Test | 25% |

## 4. Data Analyst Weighting

For Data Analyst roles:

| Evaluation Round | Weight |
|---|---:|
| ATS | 15% |
| Screening | 15% |
| HR Interview | 15% |
| Technical Interview | 25% |
| Machine Test | 30% |

## 5. Python Developer Weighting

For Python Developer roles:

| Evaluation Round | Weight |
|---|---:|
| ATS | 10% |
| Screening | 10% |
| HR Interview | 10% |
| Technical Interview | 30% |
| Machine Test | 40% |

## 6. Business Analyst Weighting

For Business Analyst roles:

| Evaluation Round | Weight |
|---|---:|
| ATS | 20% |
| Screening | 20% |
| HR Interview | 20% |
| Technical Interview | 20% |
| Machine Test | 20% |

## 7. Score Calculation

The final Hiring Fit Score is calculated by multiplying each normalized round score by its corresponding role weight.

Example:

Hiring Fit Score =

(ATS × ATS Weight)

+

(Screening × Screening Weight)

+

(HR Interview × HR Weight)

+

(Technical Interview × Technical Weight)

+

(Machine Test × Machine Test Weight)

## 8. Score Range

The final score ranges from 0 to 100.

## 9. Classification

| Score | Classification |
|---|---|
| 85-100 | Excellent Hiring Fit |
| 75-84 | Strong Hiring Fit |
| 60-74 | Moderate Hiring Fit |
| Below 60 | Low Hiring Fit |

## 10. Transparency

The system stores individual scores, weights, weighted contributions, and the final score.

This provides an explainable calculation instead of producing an unexplained final percentage.

## 11. Expected Outcome

The Hiring Fit Scoring Model provides a consistent and role-sensitive method for calculating overall candidate fit.