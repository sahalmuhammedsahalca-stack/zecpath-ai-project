class DashboardMonitor:
    def build_dashboard(self, metrics, alerts, candidate_stats, interview_stats):
        return {
            "candidate_processing": candidate_stats,
            "interview_success": interview_stats,
            "system_metrics": metrics,
            "alerts": alerts,
        }

    def candidate_processing_stats(self, total, successful, failed):
        return {
            "total_candidates": total,
            "successful": successful,
            "failed": failed,
        }

    def interview_success_stats(self, total, successful):
        success_rate = 0.0

        if total > 0:
            success_rate = (successful / total) * 100

        return {
            "total_interviews": total,
            "successful_interviews": successful,
            "success_rate_percent": round(success_rate, 2),
        }