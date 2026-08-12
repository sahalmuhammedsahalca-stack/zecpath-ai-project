# Behavioral AI Signal-to-Score Mapping

## 1. Purpose

This document defines how observable behavioral signals are mapped into behavioral evaluation scores.

The mapping provides a structured and explainable method for converting individual behavioral indicators into higher-level behavioral scores.

## 2. Input Signals

The Behavioral AI module uses the following input signals:

| Signal | Purpose |
|---|---|
| Gaze Stability | Measures consistency of visual attention |
| Head Movement | Measures observable head movement during the interview |
| Facial Engagement | Measures observable facial engagement |
| Attention Level | Measures observable attention during the interview |
| Distraction Frequency | Measures frequency of observable distractions |
| Nervous Gesture Score | Measures observable nervous gestures |

## 3. Focus Score

The focus score is calculated using:

- Gaze stability
- Attention level
- Distraction frequency

Higher gaze stability and attention contribute positively to focus.

Higher distraction frequency negatively affects focus.

## 4. Engagement Score

The engagement score considers observable signals including:

- Head movement
- Facial engagement
- Attention level

These signals are combined to produce an engagement indicator.

## 5. Behavioral Score

The behavioral score combines the major behavioral indicators.

The resulting score represents the overall observable behavioral performance during the interview.

## 6. Score Interpretation

| Score Range | Classification |
|---|---|
| 80–100 | Strong Behavioral Indicators |
| 60–79 | Moderate Behavioral Indicators |
| Below 60 | Weak Behavioral Indicators |

## 7. Example Evaluation

Example input:

- Gaze stability: 90
- Head movement: 82
- Facial engagement: 85
- Attention level: 88
- Distraction frequency: 10
- Nervous gesture score: 80

Example output:

- Focus score: 89.33
- Engagement score: 85.67
- Behavioral score: 85.0
- Classification: Strong Behavioral Indicators

## 8. Explainability

The system should retain the individual signal values together with the calculated scores.

This allows developers and reviewers to understand how the behavioral evaluation was produced.

## 9. Limitation

Behavioral scores are supporting indicators only.

They should not be interpreted as definitive evidence of candidate suitability or unsuitability.