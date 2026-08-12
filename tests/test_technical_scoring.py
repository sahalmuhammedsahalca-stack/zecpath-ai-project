from technical_interview.technical_scoring import calculate_technical_score


print("=" * 50)
print("TECHNICAL INTERVIEW SCORING")
print("=" * 50)


result = calculate_technical_score(
    technical_knowledge=90,
    practical_experience=85,
    problem_solving=88,
    conceptual_understanding=92,
    scenario_handling=87
)

print(result)


print()

result = calculate_technical_score(
    technical_knowledge=60,
    practical_experience=55,
    problem_solving=65,
    conceptual_understanding=58,
    scenario_handling=62
)

print(result)