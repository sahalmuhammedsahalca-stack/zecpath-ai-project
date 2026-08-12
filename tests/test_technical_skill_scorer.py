from technical_scoring.technical_skill_scorer import (
    calculate_technical_score,
    classify_technical_depth,
    generate_technical_evaluation
)


print("=" * 60)
print("TECHNICAL SKILL SCORING")
print("=" * 60)


# Test 1 - Strong technical performance
score = calculate_technical_score(
    accuracy=90,
    depth=88,
    logical_reasoning=92,
    real_world_applicability=90
)

print("\nTECHNICAL SCORE")
print(score)


# Test 2 - Technical depth classification
classification = classify_technical_depth(
    accuracy=90,
    depth=88,
    logical_reasoning=92,
    real_world_applicability=90
)

print("\nTECHNICAL DEPTH")
print(classification)


# Test 3 - Complete explainable evaluation
evaluation = generate_technical_evaluation(
    accuracy=90,
    depth=88,
    logical_reasoning=92,
    real_world_applicability=90
)

print("\nTECHNICAL EVALUATION")
print(evaluation)