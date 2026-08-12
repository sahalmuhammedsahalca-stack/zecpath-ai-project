\# Malpractice Detection Logic



\## 1. Purpose



This document defines the logic used to identify possible malpractice indicators during interviews.



\## 2. Input Signals



The detection logic uses:



\- Tab switching frequency

\- Screen focus loss

\- External voice detection

\- Repeated looking away



\## 3. Threshold-Based Detection



The system uses thresholds to identify unusual activity.



Examples:



\- Repeated tab switching increases integrity risk

\- Repeated screen focus loss increases integrity risk

\- External voice detection increases integrity risk

\- Repeated looking away increases integrity risk



\## 4. Risk Contribution



Each detected signal contributes to the overall integrity risk score.



The final score is limited to 0-100.



\## 5. Pattern Recognition



Multiple signals occurring together can indicate a stronger integrity concern than an isolated signal.



The system therefore retains individual flags together with the overall risk score.



\## 6. Risk Classification



| Risk Score | Classification |

| ---------- | -------------- |

| 70-100 | High Risk |

| 40-69 | Medium Risk |

| Below 40 | Low Risk |



\## 7. Flag Generation



The system generates flags for detected signals.



Possible flags include:



\- Frequent tab switching

\- Repeated screen focus loss

\- External voice detected

\- Repeated looking away



\## 8. Explainability



The system records the signals that contributed to the risk score.



This allows reviewers to understand the reason for an integrity warning.



\## 9. Limitation



Detection signals are indicators of possible malpractice.



They should not automatically be interpreted as proof of cheating.



Further review is required before making a final conclusion.

