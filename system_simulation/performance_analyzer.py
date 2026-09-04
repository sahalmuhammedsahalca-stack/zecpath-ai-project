class PerformanceAnalyzer:
    """
    Analyzes end-to-end simulation performance.
    """

    def analyze(self, simulation_result):
        stage_count = simulation_result["stage_count"]

        completed_stages = sum(
            1
            for stage in simulation_result["stages"]
            if stage["status"] in {
                "completed",
                "passed",
                "rejected",
            }
        )

        completion_rate = (
            completed_stages / stage_count * 100
            if stage_count
            else 0
        )

        return {
            "candidate_id": simulation_result["candidate_id"],
            "total_stages": stage_count,
            "completed_stages": completed_stages,
            "completion_rate": round(
                completion_rate,
                2,
            ),
            "pipeline_status": simulation_result[
                "pipeline_status"
            ],
        }