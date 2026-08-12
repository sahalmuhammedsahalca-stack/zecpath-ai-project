from ats_engine.ats_scorer import calculate_ats_score

# Scores obtained from previous modules
skill_score = 100
experience_score = 100
education_score = 70
semantic_score = 66.6

result = calculate_ats_score(
    skill_score,
    experience_score,
    education_score,
    semantic_score
)

print("=" * 50)
print("ATS FINAL SCORE")
print("=" * 50)
print(result)