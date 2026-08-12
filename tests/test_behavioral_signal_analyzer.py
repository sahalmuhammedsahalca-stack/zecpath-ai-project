from behavioral_analysis.behavioral_signal_analyzer import (
    calculate_focus_score,
    calculate_engagement_score,
    calculate_behavioral_score,
    classify_behavioral_score,
    generate_behavioral_evaluation
)


print("=" * 50)
print("BEHAVIORAL AI ANALYSIS")
print("=" * 50)


focus_score = calculate_focus_score(
    gaze_stability=90,
    attention_level=88,
    distraction_frequency=10
)

print()
print("FOCUS SCORE")
print(focus_score)


engagement_score = calculate_engagement_score(
    facial_engagement=85,
    head_movement=82,
    gaze_stability=90
)

print()
print("ENGAGEMENT SCORE")
print(engagement_score)


behavioral_score = calculate_behavioral_score(
    focus_score=focus_score,
    engagement_score=engagement_score,
    nervous_gesture_score=80
)

print()
print("BEHAVIORAL SCORE")
print(behavioral_score)


print()
print("CLASSIFICATION")
print(classify_behavioral_score(behavioral_score))


print()
print("BEHAVIORAL EVALUATION")

evaluation = generate_behavioral_evaluation(
    gaze_stability=90,
    head_movement=82,
    facial_engagement=85,
    attention_level=88,
    distraction_frequency=10,
    nervous_gesture_score=80
)

print(evaluation)