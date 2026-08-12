def calculate_focus_score(
    gaze_stability,
    attention_level,
    distraction_frequency
):
    """
    Calculate a focus score from observable interview signals.
    """

    distraction_score = max(0, 100 - distraction_frequency)

    score = (
        gaze_stability
        + attention_level
        + distraction_score
    ) / 3

    return round(score, 2)


def calculate_engagement_score(
    facial_engagement,
    head_movement,
    gaze_stability
):
    """
    Calculate an observable engagement score.
    """

    score = (
        facial_engagement
        + head_movement
        + gaze_stability
    ) / 3

    return round(score, 2)


def calculate_behavioral_score(
    focus_score,
    engagement_score,
    nervous_gesture_score
):
    """
    Calculate an overall behavioral score.

    nervous_gesture_score represents the normalized
    observable signal value supplied by the analysis layer.
    """

    score = (
        focus_score
        + engagement_score
        + nervous_gesture_score
    ) / 3

    return round(score, 2)


def classify_behavioral_score(score):
    """
    Classify the overall behavioral score.
    """

    if score >= 80:
        return "Strong Behavioral Indicators"

    elif score >= 60:
        return "Moderate Behavioral Indicators"

    else:
        return "Needs Review"


def generate_behavioral_evaluation(
    gaze_stability,
    head_movement,
    facial_engagement,
    attention_level,
    distraction_frequency,
    nervous_gesture_score
):
    """
    Generate an explainable behavioral evaluation.
    """

    focus_score = calculate_focus_score(
        gaze_stability,
        attention_level,
        distraction_frequency
    )

    engagement_score = calculate_engagement_score(
        facial_engagement,
        head_movement,
        gaze_stability
    )

    behavioral_score = calculate_behavioral_score(
        focus_score,
        engagement_score,
        nervous_gesture_score
    )

    classification = classify_behavioral_score(
        behavioral_score
    )

    return {
        "gaze_stability": gaze_stability,
        "head_movement": head_movement,
        "facial_engagement": facial_engagement,
        "attention_level": attention_level,
        "distraction_frequency": distraction_frequency,
        "nervous_gesture_score": nervous_gesture_score,
        "focus_score": focus_score,
        "engagement_score": engagement_score,
        "behavioral_score": behavioral_score,
        "classification": classification,
        "explanation": (
            "Behavioral evaluation is based on observable "
            "interview signals and is intended as a supporting "
            "indicator rather than a standalone hiring decision."
        )
    }