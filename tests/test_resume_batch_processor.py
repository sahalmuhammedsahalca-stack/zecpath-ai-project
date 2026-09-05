from performance_scaling.resume_batch_processor import ResumeBatchProcessor


def test_batch_creation():

    processor = ResumeBatchProcessor(
        batch_size=2
    )

    batches = processor.create_batches(
        [1, 2, 3, 4, 5]
    )

    assert batches == [
        [1, 2],
        [3, 4],
        [5],
    ]


def test_resume_processing():

    processor = ResumeBatchProcessor(
        batch_size=2
    )

    results = processor.process(
        [1, 2, 3],
        lambda resume: resume * 10,
    )

    assert results == [
        10,
        20,
        30,
    ]