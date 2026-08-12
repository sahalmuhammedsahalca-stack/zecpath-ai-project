def generate_risk_flag(risk_score):
    """
    Generate a risk flag from the integrity risk score.
    """

    if risk_score >= 70:
        return {
            "risk_tag": "HIGH_INTEGRITY_RISK",
            "alert_level": "Immediate Review"
        }

    elif risk_score >= 40:
        return {
            "risk_tag": "MEDIUM_INTEGRITY_RISK",
            "alert_level": "Review Required"
        }

    else:
        return {
            "risk_tag": "LOW_INTEGRITY_RISK",
            "alert_level": "No Immediate Alert"
        }


def generate_alert_message(risk_score):
    """
    Generate an alert message for the interview monitoring system.
    """

    if risk_score >= 70:
        return "High integrity risk detected. Immediate review recommended."

    elif risk_score >= 40:
        return "Moderate integrity risk detected. Review required."

    else:
        return "No significant integrity risk detected."