from parsers.pdf_reader import extract_text_from_pdf
from parsers.text_cleaner import clean_text
from parsers.experience_parser import parse_experience
from parsers.experience_calculator import calculate_total_experience
from parsers.gap_detector import detect_gap
from ats_engine.role_relevance import calculate_role_relevance
from parsers.json_writer import save_json

# Resume PDF
pdf_path = "data/resumes/raw_resumes/Sahal Mohd CV.pdf"

resume_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(resume_text)

experience = parse_experience(cleaned_text)
total_exp = calculate_total_experience(experience)
gaps = detect_gap(experience)
role_scores = calculate_role_relevance(
    experience,
    "Data Analyst"
)
experience_report = {
    "experience": experience,
    "total_experience": total_exp,
    "employment_gaps": gaps,
    "role_relevance": role_scores
}

output_path = "data/resumes/processed_resumes/experience_analysis.json"

save_json(experience_report, output_path)

print("=" * 50)
print("EXPERIENCE PARSER OUTPUT")
print("=" * 50)
print(experience)

print()
print("=" * 50)
print("EMPLOYMENT GAPS")
print("=" * 50)
print(gaps)

print()
print("=" * 50)
print("TOTAL EXPERIENCE")
print("=" * 50)
print(total_exp)

print()

print("=" * 50)
print("ROLE RELEVANCE")
print("=" * 50)
print(role_scores)