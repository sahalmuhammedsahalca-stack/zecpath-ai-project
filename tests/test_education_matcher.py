from parsers.resume_parser import parse_resume
from parsers.jd_parser import parse_job_description

from parsers.pdf_reader import extract_text_from_pdf
from ats_engine.education_matcher import calculate_education_match
from parsers.json_writer import save_json
from ats_engine.education_score import calculate_education_score


# Resume
pdf_path = "data/resumes/raw_resumes/Sahal Mohd CV.pdf"
resume_text = extract_text_from_pdf(pdf_path)

resume_data = parse_resume(resume_text)


# Job Description
with open(
    "data/job_descriptions/raw_job_descriptions/data_analyst_jd.txt",
    "r",
    encoding="utf-8"
) as file:
    jd_text = file.read()

jd_data = parse_job_description(jd_text)


# Match Education
result = calculate_education_match(
    resume_data["education"],
    jd_data["education"]
)
education_score = calculate_education_score(result)
output_path = (
    "data/resumes/processed_resumes/"
    "education_analysis.json"
)

save_json(result, output_path)


print("=" * 50)
print("EDUCATION MATCH")
print("=" * 50)
print(result)

print()

print("=" * 50)
print("FINAL EDUCATION SCORE")
print("=" * 50)
print(education_score)