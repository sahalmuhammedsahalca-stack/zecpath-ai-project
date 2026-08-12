from confidence_analysis.hesitation_detector import hesitation
from confidence_analysis.uncertainty_detector import uncertainty
from confidence_analysis.sentiment_analyzer import sentiment
from confidence_analysis.contradiction_detector import contradiction
from confidence_analysis.stress_detector import stress
from confidence_analysis.confidence_score import calculate


def evaluate(answer):

    scores = [
        hesitation(answer),
        uncertainty(answer),
        sentiment(answer),
        contradiction(answer),
        stress(answer)
    ]

    return {
        "Hesitation": scores[0],
        "Uncertainty": scores[1],
        "Sentiment": scores[2],
        "Contradiction": scores[3],
        "Stress": scores[4],
        "Confidence Score": calculate(scores)
    }