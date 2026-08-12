def calculate_integrity_risk(
    tab_switch_count,
    screen_focus_loss_count,
    external_voice_detected,
    looking_away_count
):
    """
    Calculate an interview integrity risk score
    from observable malpractice indicators.
    """

    risk_score = 0

    if tab_switch_count >= 5:
        risk_score += 25
    elif tab_switch_count >= 3:
        risk_score += 15

    if screen_focus_loss_count >= 5:
        risk_score += 25
    elif screen_focus_loss_count >= 3:
        risk_score += 15

    if external_voice_detected:
        risk_score += 30

    if looking_away_count >= 8:
        risk_score += 20
    elif looking_away_count >= 5:
        risk_score += 10

    return min(risk_score, 100)


def classify_integrity_risk(risk_score):
    """
    Classify the integrity risk level.
    """

    if risk_score >= 70:
        return "High Risk"

    elif risk_score >= 40:
        return "Medium Risk"

    else:
        return "Low Risk"


def generate_integrity_evaluation(
    tab_switch_count,
    screen_focus_loss_count,
    external_voice_detected,
    looking_away_count
):
    """
    Generate an explainable integrity evaluation.
    """

    risk_score = calculate_integrity_risk(
        tab_switch_count,
        screen_focus_loss_count,
        external_voice_detected,
        looking_away_count
    )

    classification = classify_integrity_risk(risk_score)

    flags = []

    if tab_switch_count >= 3:
        flags.append("Frequent tab switching")

    if screen_focus_loss_count >= 3:
        flags.append("Repeated screen focus loss")

    if external_voice_detected:
        flags.append("External voice detected")

    if looking_away_count >= 5:
        flags.append("Repeated looking away")

    return {
        "tab_switch_count": tab_switch_count,
        "screen_focus_loss_count": screen_focus_loss_count,
        "external_voice_detected": external_voice_detected,
        "looking_away_count": looking_away_count,
        "integrity_risk_score": risk_score,
        "risk_classification": classification,
        "flags": flags,
        "explanation": (
            "Integrity risk is based on observable interview signals "
            "and should be reviewed together with other evidence."
        )
    }