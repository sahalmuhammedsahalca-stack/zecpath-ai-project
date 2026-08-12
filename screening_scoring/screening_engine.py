from screening_scoring.question_scorer import score_question
from screening_scoring.score_aggregator import aggregate_scores
from screening_scoring.explanation_generator import generate_explanation


def evaluate_screening():

    question_scores = [
        score_question(22, 24, 21, 23),
        score_question(20, 22, 23, 21),
        score_question(24, 23, 24, 25)
    ]

    final = aggregate_scores(question_scores)

    return {
        "question_scores": question_scores,
        "final_score": final,
        "explanation": generate_explanation(
            final["normalized_score"]
        )
    }