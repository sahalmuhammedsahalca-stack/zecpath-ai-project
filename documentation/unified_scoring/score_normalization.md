# Cross-Round Score Normalization

## 1. Purpose

Score normalization ensures that all recruitment evaluation scores are represented consistently on a 0-100 scale.

## 2. Input

The normalization system accepts scores from:

- ATS
- Screening
- HR Interview
- Technical Interview
- Machine Test

## 3. Normalization Range

All scores are restricted to:

0-100

## 4. Validation

The system converts numeric values into floating-point scores.

Invalid non-numeric values are rejected.

## 5. Boundary Handling

Scores above 100 are limited to 100.

Scores below 0 are limited to 0.

Examples:

| Input | Normalized Score |
|---:|---:|
| 105 | 100 |
| 90 | 90 |
| 50 | 50 |
| -10 | 0 |

## 6. Purpose in Aggregation

Normalization ensures that every evaluation round contributes to the final Hiring Fit Score using a consistent scale.

## 7. Transparency

Both original scores and normalized scores are retained in the unified candidate score object.

## 8. Expected Outcome

The normalization component provides a consistent foundation for role-based weighted aggregation across different recruitment stages.