def calculate_hiring_fit(unified_score):

    if unified_score >= 85:
        fit = "Excellent Fit"
    elif unified_score >= 70:
        fit = "Good Fit"
    elif unified_score >= 60:
        fit = "Moderate Fit"
    else:
        fit = "Low Fit"

    return {
        "hiring_fit_percentage": round(unified_score, 2),
        "fit_category": fit
    }