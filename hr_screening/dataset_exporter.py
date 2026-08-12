import json
import os

from hr_screening.question_bank import QUESTION_BANK

def export_dataset():

    output_folder = "data/hr_screening"

    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(
        output_folder,
        "hr_question_dataset.json"
    )

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            QUESTION_BANK,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"Dataset exported to: {output_file}")