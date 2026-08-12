def generate_explanation(score):

    if score >= 85:
        return "Excellent screening performance."

    elif score >= 70:
        return "Good screening performance."

    elif score >= 50:
        return "Average screening performance."

    else:
        return "Needs improvement."