\# Risk Flagging System Design



\## 1. Purpose



The Risk Flagging System converts integrity-risk scores into structured interview risk tags and warning levels.



\## 2. Risk Levels



\### Low Risk



Risk score below 40.



Action:



\- No immediate alert

\- Continue monitoring



\### Medium Risk



Risk score from 40 to 69.



Action:



\- Generate review-required alert

\- Continue monitoring



\### High Risk



Risk score from 70 to 100.



Action:



\- Generate immediate-review alert

\- Mark the interview for further review



\## 3. Risk Tags



The system generates:



\- LOW\_INTEGRITY\_RISK

\- MEDIUM\_INTEGRITY\_RISK

\- HIGH\_INTEGRITY\_RISK



\## 4. Real-Time Alerts



The system can generate warning messages when the integrity risk reaches a defined threshold.



Examples:



\- High integrity risk detected

\- Moderate integrity risk detected

\- No significant integrity risk detected



\## 5. Interview Risk Tagging



The risk tag can be attached to the interview evaluation record.



This allows the wider recruitment system to identify interviews requiring review.



\## 6. Behavioral Integration



Integrity risk information may be combined with behavioral analysis information to provide wider interview context.



The two systems should remain separate so that behavioral observations do not automatically prove malpractice.



\## 7. Human Review



Risk flags require appropriate review.



A risk flag is an indicator and not definitive proof of malpractice.



\## 8. Expected Outcome



The Risk Flagging System provides structured alerts and interview risk tags that allow suspicious activity to be identified and reviewed systematically.

