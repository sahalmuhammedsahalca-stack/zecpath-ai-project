import pdfplumber


def extract_text_from_pdf(pdf_path):
    """
    Reads a PDF resume and extracts all text.
    """

    extracted_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                extracted_text += text + "\n"

    return extracted_text