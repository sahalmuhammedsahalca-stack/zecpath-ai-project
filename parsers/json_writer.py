import json
import os


def save_json(data, output_path):
    """
    Saves Python dictionary as JSON.
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"JSON saved successfully: {output_path}")