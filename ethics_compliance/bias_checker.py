DEMOGRAPHIC_SIGNALS = [
    "gender",
    "religion",
    "caste",
    "race",
    "ethnicity",
    "age"
]


def remove_demographic_signals(data):

    cleaned_data = {}

    for key, value in data.items():

        if key.lower() not in DEMOGRAPHIC_SIGNALS:
            cleaned_data[key] = value

    return cleaned_data