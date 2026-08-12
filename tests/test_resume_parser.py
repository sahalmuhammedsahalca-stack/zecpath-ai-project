from parsers.pdf_reader import extract_text_from_pdf
from parsers.text_cleaner import clean_text
from parsers.resume_parser import parse_resume
from parsers.json_writer import save_json

# Read Resume PDF
pdf_path = "data/resumes/raw_resumes/Sahal Mohd CV.pdf"

resume_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(resume_text)

# Parse Resume
resume_data = parse_resume(cleaned_text)

# Save Resume JSON
output_path = "data/resumes/processed_resumes/sample_resume.json"
save_json(resume_data, output_path)

print("=" * 50)
print("RESUME PARSER OUTPUT")
print("=" * 50)
print(resume_data)