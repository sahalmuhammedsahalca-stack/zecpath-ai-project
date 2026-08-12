import json
import os


def export_transcript(data):

    output_folder = "data/transcripts"

    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(
        output_folder,
        "screening_transcript.json"
    )

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"Transcript exported to: {output_file}")