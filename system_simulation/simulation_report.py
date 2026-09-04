class SimulationReport:
    """
    Generates the final end-to-end simulation report.
    """

    def generate(
        self,
        simulation_result,
        comparison,
        consistency,
        performance,
    ):
        return {
            "candidate_id": simulation_result["candidate_id"],
            "pipeline_status": simulation_result[
                "pipeline_status"
            ],
            "final_decision": simulation_result["stages"][-1][
                "decision"
            ],
            "ai_score": simulation_result["stages"][-1][
                "overall_score"
            ],
            "human_score": comparison["human_score"],
            "score_difference": comparison[
                "score_difference"
            ],
            "decision_match": comparison["decision_match"],
            "consistency_status": consistency["status"],
            "inconsistencies": consistency[
                "inconsistencies"
            ],
            "completion_rate": performance[
                "completion_rate"
            ],
        }