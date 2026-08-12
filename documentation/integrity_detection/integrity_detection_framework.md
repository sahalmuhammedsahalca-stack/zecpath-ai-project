\# Integrity Detection Framework



\## 1. Purpose



The Integrity Detection Framework defines the processing structure used to identify possible malpractice or external assistance during an interview.



The framework uses observable interview signals to generate structured integrity-risk information.



\## 2. Malpractice Signals



The system considers the following signals:



\- Tab switching frequency

\- Loss of screen focus

\- External voice detection

\- Repeated looking away



\## 3. Signal Collection



The system receives observable interview monitoring signals.



Each signal is recorded for evaluation by the integrity detection module.



\## 4. Signal Analysis



The system evaluates the frequency or presence of each signal.



Examples:



\- Frequent tab switching

\- Repeated screen focus loss

\- External voice presence

\- Repeated looking away



\## 5. Risk Calculation



The detected signals contribute to an overall integrity risk score.



The risk score is limited to a range of 0-100.



\## 6. Risk Classification



| Score Range | Classification |

| ----------- | -------------- |

| 70-100 | High Risk |

| 40-69 | Medium Risk |

| Below 40 | Low Risk |



\## 7. Risk Flags



Detected signals may generate specific risk flags.



Examples:



\- Frequent tab switching

\- Repeated screen focus loss

\- External voice detected

\- Repeated looking away



\## 8. Warning System



The system can generate different warning levels:



\- Immediate Review

\- Review Required

\- No Immediate Alert



\## 9. Behavioral Integration



Integrity signals can be considered together with behavioral analysis results.



Behavioral indicators should provide supporting context rather than automatically determining whether malpractice occurred.



\## 10. Explainability



The system retains:



\- Individual signal values

\- Integrity risk score

\- Risk classification

\- Detected flags

\- Alert level



This allows reviewers to understand why an integrity risk was generated.



\## 11. Human Review



Integrity flags represent indicators requiring review.



A flag should not automatically be treated as proof of cheating or malpractice.



\## 12. Expected Outcome



The framework provides a structured method for monitoring observable interview integrity signals and generating explainable risk information for further review.

