def analyze_sentiment(text):

    text = text.lower()

    positive = ["good", "excellent", "confident", "happy", "yes"]
    negative = ["bad", "difficult", "problem", "no", "confused"]

    score = 0

    for word in positive:
        if word in text:
            score += 1

    for word in negative:
        if word in text:
            score -= 1

    if score > 0:
        return "Positive"

    elif score < 0:
        return "Negative"

    return "Neutral"