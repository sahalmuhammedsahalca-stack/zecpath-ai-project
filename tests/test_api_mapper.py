from api_integration.api_mapper import APIMapper


def test_all_api_mappings():

    api_names = [
        "resume_parsing",
        "ats_scoring",
        "screening",
        "interview",
        "decision",
    ]

    for api_name in api_names:
        assert APIMapper.validate_mapping(api_name)


def test_interview_mapping():

    mapping = APIMapper.get_mapping("interview")

    assert mapping["ai_service"] == "interview_ai"
    assert mapping["database_target"] == "interview_scores"