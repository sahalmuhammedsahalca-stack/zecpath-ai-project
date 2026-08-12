def rank_candidates(candidates):
    """
    Sort candidates based on ATS score
    in descending order.
    """

    ranked = sorted(
        candidates,
        key=lambda x: x["final_score"],
        reverse=True
    )

    return ranked