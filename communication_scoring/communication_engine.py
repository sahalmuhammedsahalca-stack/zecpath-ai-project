from communication_scoring.score_calculator import calculate_score
from communication_scoring.recommendation_engine import recommend
from communication_scoring.communication_report import generate_report


def evaluate(confidence, sentiment, hesitation):

    score = calculate_score(
        confidence,
        sentiment,
        hesitation
    )

    recommendation = recommend(score)

    return generate_report(score, recommendation)