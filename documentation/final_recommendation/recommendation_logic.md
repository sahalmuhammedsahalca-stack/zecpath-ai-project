\# Recommendation Logic



\## 1. Purpose



The Recommendation Logic defines the rules used to generate the final hiring recommendation.



\## 2. Decision Categories



The system produces:



\- Selected

\- Hold / Review

\- Rejected



\## 3. Selected Rule



A candidate is Selected when:



\- Overall score is 80 or above

\- Behavioral score is 70 or above

\- Integrity risk is below 80



\## 4. Hold / Review Rule



A candidate is placed on Hold / Review when:



\- Overall score is 60 or above

\- Behavioral score is 60 or above

\- No high integrity risk condition is triggered



\## 5. Rejected Rule



A candidate is Rejected when:



\- Integrity risk score is 80 or above



or



\- Overall performance does not meet the minimum requirements.



\## 6. Hybrid Logic



The system combines numerical scores with rule-based risk conditions.



This prevents the final decision from depending only on the overall candidate score.



\## 7. Explainability



The recommendation is returned together with the candidate scores, risk factors, confidence score, and explanation.



\## 8. Expected Outcome



The Recommendation Logic provides a consistent method for converting candidate performance and risk information into a final hiring recommendation.

