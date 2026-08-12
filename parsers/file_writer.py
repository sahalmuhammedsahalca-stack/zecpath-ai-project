import os


def save_text(text, output_path):
    """
    Saves cleaned resume text into a text file.
    """

    # Create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the text into the file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"File saved successfully: {output_path}")