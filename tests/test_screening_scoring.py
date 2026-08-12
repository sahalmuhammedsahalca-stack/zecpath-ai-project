from screening_scoring.screening_engine import evaluate_screening

result = evaluate_screening()

print("=" * 60)
print("SCREENING SCORING ENGINE")
print("=" * 60)

print("\nPer Question Scores")

for i, score in enumerate(result["question_scores"], start=1):
    print(f"Question {i}: {score}")

print("\nFinal Score")
print(result["final_score"])

print("\nExplanation")
print(result["explanation"])