from api_integration.integration_controller import IntegrationController


def test_complete_integration_plan():

    result = IntegrationController.build_integration_plan()

    assert result["status"] == "proposed"

    assert "resume_parsing" in result["apis"]
    assert "ats_scoring" in result["apis"]
    assert "screening" in result["apis"]
    assert "interview" in result["apis"]
    assert "decision" in result["apis"]

    assert result["security"]["authentication_required"] is True