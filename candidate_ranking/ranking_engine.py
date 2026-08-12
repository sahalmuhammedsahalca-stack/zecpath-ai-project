from candidate_ranking.weighted_score import final_score
from candidate_ranking.recommendation import recommendation
from candidate_ranking.rank_sorter import sort_candidates

def rank(candidates):

    results = []

    for candidate in candidates:

        score = final_score(
            candidate["ats"],
            candidate["interview"],
            candidate["communication"],
            candidate["confidence"]
        )

        results.append({
            "name": candidate["name"],
            "final_score": score,
            "recommendation": recommendation(score)
        })

    return sort_candidates(results)