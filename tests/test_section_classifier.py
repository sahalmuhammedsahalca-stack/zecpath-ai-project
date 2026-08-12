from parsers.pdf_reader import extract_text_from_pdf
from parsers.text_cleaner import clean_text
from parsers.section_classifier import classify_sections
from parsers.json_writer import save_json

# Read Resume PDF
pdf_path = "data/resumes/raw_resumes/Sahal Mohd CV.pdf"

resume_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(resume_text)

# Classify Sections
sections = classify_sections(cleaned_text)

# Save as JSON
output_path = "data/resumes/processed_resumes/resume_sections.json"
save_json(sections, output_path)

print("=" * 50)
print("RESUME SECTION CLASSIFIER OUTPUT")
print("=" * 50)
print(sections)