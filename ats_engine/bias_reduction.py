import re

def mask_personal_information(resume_data):
    """
    Masks non-essential personal information
    to reduce bias during evaluation.
    """

    masked_data = resume_data.copy()

    # Mask personal details
    masked_data["name"] = "[MASKED]"
    masked_data["email"] = "[MASKED]"
    masked_data["phone"] = "[MASKED]"

    return masked_data