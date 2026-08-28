\# Candidate Decision Output Format



\## 1. Purpose



The Candidate Decision Output Format defines the structured information returned by the Final Recommendation AI.



\## 2. Output Fields



The system returns:



\- Candidate ID

\- Candidate name

\- Overall score

\- Behavioral score

\- Integrity risk score

\- Recommendation

\- Confidence score

\- Risk factors

\- Explanation



\## 3. Recommendation Values



The recommendation field can contain:



\- Selected

\- Hold / Review

\- Rejected



\## 4. Confidence Score



The confidence score is represented on a scale of 0 to 100.



Higher confidence indicates stronger agreement between the candidate scores and risk indicators.



\## 5. Risk Factors



Risk factors provide additional information that may affect the final decision.



Examples include:



\- Behavioral concerns

\- High integrity risk

\- No major risk factors detected



\## 6. Example Output



```text

Candidate ID: CAND001

Candidate Name: Test Candidate

Overall Score: 88

Behavioral Score: 85

Integrity Risk Score: 10

Recommendation: Selected

Confidence Score: 87.67

Risk Factors: No major risk factors detected

