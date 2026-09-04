from api_integration.api_registry import APIRegistry


def test_api_registry_contains_required_apis():

    apis = APIRegistry.list_apis()

    assert "resume_parsing" in apis
    assert "ats_scoring" in apis
    assert "screening" in apis
    assert "interview" in apis
    assert "decision" in apis


def test_resume_api_definition():

    api = APIRegistry.get_api("resume_parsing")

    assert api["method"] == "POST"
    assert api["processing"] == "async"