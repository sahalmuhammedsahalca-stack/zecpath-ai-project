from datetime import datetime, timezone


class FullSystemSimulator:
    """
    Simulates the complete Zecpath AI hiring journey.
    """

    def __init__(self):
        self.stages = [
            "resume_upload",
            "ats_scoring",
            "screening",
            "hr_interview",
            "technical_interview",
            "final_decision",
        ]

    def simulate_resume_upload(self, candidate):
        return {
            "stage": "resume_upload",
            "status": "completed",
            "candidate_id": candidate["candidate_id"],
            "resume_file": candidate["resume_file"],
        }

    def simulate_ats_scoring(self, candidate):
        return {
            "stage": "ats_scoring",
            "status": "completed",
            "candidate_id": candidate["candidate_id"],
            "score": candidate["ats_score"],
        }

    def simulate_screening(self, candidate):
        status = (
            "passed"
            if candidate["screening_score"] >= 60
            else "rejected"
        )

        return {
            "stage": "screening",
            "status": status,
            "candidate_id": candidate["candidate_id"],
            "score": candidate["screening_score"],
        }

    def simulate_hr_interview(self, candidate):
        return {
            "stage": "hr_interview",
            "status": "completed",
            "candidate_id": candidate["candidate_id"],
            "score": candidate["hr_score"],
        }

    def simulate_technical_interview(self, candidate):
        return {
            "stage": "technical_interview",
            "status": "completed",
            "candidate_id": candidate["candidate_id"],
            "score": candidate["technical_score"],
        }

    def simulate_final_decision(self, candidate):
        scores = [
            candidate["ats_score"],
            candidate["screening_score"],
            candidate["hr_score"],
            candidate["technical_score"],
        ]

        overall_score = sum(scores) / len(scores)

        if overall_score >= 85:
            decision = "Highly Recommended"
        elif overall_score >= 70:
            decision = "Recommended"
        elif overall_score >= 60:
            decision = "Needs Review"
        else:
            decision = "Not Recommended"

        return {
            "stage": "final_decision",
            "status": "completed",
            "candidate_id": candidate["candidate_id"],
            "overall_score": round(overall_score, 2),
            "decision": decision,
        }

    def run(self, candidate):
        start_time = datetime.now(timezone.utc)

        results = [
            self.simulate_resume_upload(candidate),
            self.simulate_ats_scoring(candidate),
            self.simulate_screening(candidate),
            self.simulate_hr_interview(candidate),
            self.simulate_technical_interview(candidate),
        ]

        final_decision = self.simulate_final_decision(candidate)
        results.append(final_decision)

        end_time = datetime.now(timezone.utc)

        return {
            "candidate_id": candidate["candidate_id"],
            "started_at": start_time.isoformat(),
            "completed_at": end_time.isoformat(),
            "stages": results,
            "stage_count": len(results),
            "pipeline_status": "completed",
        }