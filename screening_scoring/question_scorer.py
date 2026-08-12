from screening_scoring.scoring_parameters import PARAMETERS

def score_question(clarity, relevance, completeness, consistency):

    return {
        "Clarity": clarity,
        "Relevance": relevance,
        "Completeness": completeness,
        "Consistency": consistency,
        "Total": clarity + relevance + completeness + consistency,
        "Max": sum(PARAMETERS.values())
    }