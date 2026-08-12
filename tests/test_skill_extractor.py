from parsers.pdf_reader import extract_text_from_pdf
from parsers.text_cleaner import clean_text
from parsers.skill_extractor import extract_skills
from parsers.skill_confidence import assign_confidence
from parsers.json_writer import save_json

pdf_path = "data/resumes/raw_resumes/Sahal Mohd CV.pdf"

resume_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(resume_text)

skills = extract_skills(cleaned_text)
skill_scores = assign_confidence(skills)

output_path = "data/resumes/processed_resumes/skills.json"
save_json(skill_scores, output_path)

print("=" * 50)
print("SKILL EXTRACTION OUTPUT")
print("=" * 50)
print(skill_scores)