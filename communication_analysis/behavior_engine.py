from communication_analysis.hesitation_detector import detect_hesitation
from communication_analysis.sentiment_analyzer import analyze_sentiment
from communication_analysis.confidence_analyzer import analyze_confidence
from communication_analysis.communication_metrics import communication_metrics


def analyze_behavior(response):

    return {
        "hesitation_count": detect_hesitation(response),
        "sentiment": analyze_sentiment(response),
        "confidence": analyze_confidence(response),
        "metrics": communication_metrics(response)
    }