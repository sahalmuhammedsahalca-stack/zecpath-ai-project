import json
from pathlib import Path


class DemoHiringPipeline:
    def __init__(self, dataset_root=None):
        if dataset_root is None:
            dataset_root = Path(__file__).resolve().parents[1]

        self.dataset_root = Path(dataset_root)

    def load_json(self, relative_path):
        path = self.dataset_root / relative_path

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def load_pipeline(self):
        return self.load_json(
            "pipeline/complete_hiring_pipeline.json"
        )

    def get_candidate(self, candidate_id):
        data = self.load_pipeline()

        return data["candidates"].get(candidate_id)

    def run_candidate(self, candidate_id):
        candidate = self.get_candidate(candidate_id)

        if candidate is None:
            return {
                "status": "error",
                "message": "Candidate not found",
            }

        return {
            "status": "success",
            "candidate_id": candidate_id,
            "pipeline_completed": True,
            "results": candidate,
        }

    def run_all(self):
        data = self.load_pipeline()

        results = {}

        for candidate_id in data["candidates"]:
            results[candidate_id] = self.run_candidate(
                candidate_id
            )

        return results


if __name__ == "__main__":
    pipeline = DemoHiringPipeline()

    results = pipeline.run_all()

    print("=" * 60)
    print("DAY 63 DEMO HIRING PIPELINE")
    print("=" * 60)

    for candidate_id, result in results.items():
        print(candidate_id, "->", result["status"])

    print("=" * 60)
    print("DEMO PIPELINE COMPLETED")
    print("=" * 60)