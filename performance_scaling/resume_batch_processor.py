from typing import Callable, List, Any


class ResumeBatchProcessor:
    """Processes resumes in configurable batches."""

    def __init__(self, batch_size: int = 10):

        if batch_size <= 0:
            raise ValueError(
                "batch_size must be greater than zero"
            )

        self.batch_size = batch_size

    def create_batches(
        self,
        resumes: List[Any],
    ):
        return [
            resumes[i:i + self.batch_size]
            for i in range(
                0,
                len(resumes),
                self.batch_size,
            )
        ]

    def process(
        self,
        resumes: List[Any],
        processor: Callable[[Any], Any],
    ):
        results = []

        for batch in self.create_batches(resumes):

            for resume in batch:
                results.append(
                    processor(resume)
                )

        return results

    def summary(
        self,
        resumes: List[Any],
    ):
        batches = self.create_batches(resumes)

        return {
            "resume_count": len(resumes),
            "batch_size": self.batch_size,
            "batch_count": len(batches),
        }