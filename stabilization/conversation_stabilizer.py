class ConversationStabilizer:
    """
    Validates conversation flow and prevents invalid
    interview-state transitions.
    """

    VALID_STATES = {
        "started",
        "questioning",
        "completed",
        "terminated",
    }

    VALID_TRANSITIONS = {
        "started": {"questioning", "terminated"},
        "questioning": {"questioning", "completed", "terminated"},
        "completed": set(),
        "terminated": set(),
    }

    def validate_state(self, state):
        if state not in self.VALID_STATES:
            raise ValueError(
                f"Invalid conversation state: {state}"
            )

        return True

    def can_transition(self, current_state, next_state):
        self.validate_state(current_state)
        self.validate_state(next_state)

        return next_state in self.VALID_TRANSITIONS[
            current_state
        ]

    def transition(self, current_state, next_state):
        if not self.can_transition(
            current_state,
            next_state,
        ):
            raise ValueError(
                f"Invalid transition: "
                f"{current_state} -> {next_state}"
            )

        return next_state