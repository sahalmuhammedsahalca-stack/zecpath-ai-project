import json
import os


def save_json(data, output_path):
    """
    Saves dictionary data into a JSON file.
    """

    folder = os.path.dirname(output_path)

    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"JSON saved successfully: {output_path}")