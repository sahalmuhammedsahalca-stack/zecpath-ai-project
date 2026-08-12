from ethics_compliance.consent_requirements import get_consent_requirements
from ethics_compliance.fairness_review import review_score_fairness
from ethics_compliance.bias_checker import remove_demographic_signals
from ethics_compliance.explainability import generate_explanation
from ethics_compliance.data_retention import get_retention_policy


print("=" * 60)
print("DAY 43 - ETHICS & COMPLIANCE REVIEW")
print("=" * 60)

print("\nCONSENT REQUIREMENTS")
print(get_consent_requirements())

print("\nFAIRNESS REVIEW")
print(review_score_fairness([88.82, 90.67, 90]))

print("\nBIAS CHECK")

candidate_data = {
    "name": "Muhammed Sahal",
    "skills": ["Python", "SQL"],
    "gender": "Male",
    "age": 25
}

print(remove_demographic_signals(candidate_data))

print("\nEXPLAINABILITY")

scores = {
    "ats_score": 88.82,
    "screening_score": 90.67,
    "hr_interview_score": 90
}

print(generate_explanation(scores))

print("\nDATA RETENTION")
print(get_retention_policy())

print("=" * 60)