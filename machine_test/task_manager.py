def create_machine_test(
    role,
    task_type,
    difficulty,
    required_skills,
    time_limit
):
    """
    Create a structured machine test definition.
    """

    return {
        "role": role,
        "task_type": task_type,
        "difficulty": difficulty,
        "required_skills": required_skills,
        "time_limit_minutes": time_limit,
        "status": "Test Created"
    }


def validate_task_type(task_type):
    """
    Validate supported machine test task types.
    """

    supported_types = [
        "coding",
        "debugging",
        "file_based",
        "system_design"
    ]

    return task_type in supported_types