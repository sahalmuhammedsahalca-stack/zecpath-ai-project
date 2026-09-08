from feature_polish.feature_polish_controller import FeaturePolishController


controller = FeaturePolishController()

result = controller.process_candidate(
    candidate_id="CAND001",
    scores={
        "ATS": 92,
        "Screening": 90,
        "HR": 88,
        "Technical": 91,
    },
    recommendation="Highly Recommended",
    strengths=[
        "Strong technical skills",
        "Relevant experience",
        "Consistent evaluation results",
    ],
    concerns=[],
)

print("=" * 60)
print("DAY 65 - FEATURE POLISH DEMONSTRATION")
print("=" * 60)
print(result)
print("=" * 60)
print("FEATURE POLISH COMPLETED")
print("=" * 60)
