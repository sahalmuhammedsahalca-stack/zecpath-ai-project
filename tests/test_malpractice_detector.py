from integrity_detection.malpractice_detector import (
    calculate_integrity_risk,
    classify_integrity_risk,
    generate_integrity_evaluation
)


print("=" * 50)
print("MALPRACTICE & INTEGRITY DETECTION")
print("=" * 50)


print("\nINTEGRITY RISK SCORE")

risk_score = calculate_integrity_risk(
    tab_switch_count=6,
    screen_focus_loss_count=5,
    external_voice_detected=True,
    looking_away_count=8
)

print(risk_score)


print("\nRISK CLASSIFICATION")

print(
    classify_integrity_risk(risk_score)
)


print("\nINTEGRITY EVALUATION")

evaluation = generate_integrity_evaluation(
    tab_switch_count=6,
    screen_focus_loss_count=5,
    external_voice_detected=True,
    looking_away_count=8
)

print(evaluation)