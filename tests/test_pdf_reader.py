from parsers.pdf_reader import extract_text_from_pdf
from parsers.text_cleaner import clean_text
from parsers.file_writer import save_text

# Path to your resume PDF
pdf_path = "data/resumes/raw_resumes/Sahal Mohd CV.pdf"

# Output text file
output_path = "data/processed_resumes/Sahal Mohd CV.txt"

# Step 1: Extract text
raw_text = extract_text_from_pdf(pdf_path)

# Step 2: Clean text
cleaned_text = clean_text(raw_text)

# Step 3: Save cleaned text
save_text(cleaned_text, output_path)

print("\nResume processing completed successfully!")