from api_integration.processing_strategy import ProcessingStrategy


def test_resume_processing_is_async():

    assert ProcessingStrategy.is_async("resume_parsing")


def test_interview_processing_is_sync():

    assert ProcessingStrategy.is_sync("interview")


def test_decision_processing_is_sync():

    assert ProcessingStrategy.is_sync("decision")