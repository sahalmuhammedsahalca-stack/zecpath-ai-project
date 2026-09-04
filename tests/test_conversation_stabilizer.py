from stabilization.conversation_stabilizer import (
    ConversationStabilizer,
)


def test_valid_transition():
    stabilizer = ConversationStabilizer()

    assert stabilizer.transition(
        "started",
        "questioning",
    ) == "questioning"


def test_questioning_to_completed():
    stabilizer = ConversationStabilizer()

    assert stabilizer.transition(
        "questioning",
        "completed",
    ) == "completed"


def test_invalid_transition():
    stabilizer = ConversationStabilizer()

    try:
        stabilizer.transition(
            "completed",
            "questioning",
        )
        assert False
    except ValueError:
        assert True


def test_invalid_state():
    stabilizer = ConversationStabilizer()

    try:
        stabilizer.validate_state("unknown")
        assert False
    except ValueError:
        assert True