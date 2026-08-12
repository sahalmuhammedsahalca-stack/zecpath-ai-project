from parsers.pdf_reader import extract_text_from_pdf
from parsers.jd_parser import parse_job_description
from ats_engine.semantic_matcher import calculate_semantic_similarity
from utils.json_writer import save_json

# Resume
pdf_path = "data/resumes/raw_resumes/Sahal Mohd CV.pdf"
resume_text = extract_text_from_pdf(pdf_path)

# Job Description
with open(
    "data/job_descriptions/raw_job_descriptions/data_analyst_jd.txt",
    "r",
    encoding="utf-8"
) as file:
    jd_text = file.read()

jd_data = parse_job_description(jd_text)

# Semantic Matching
result = calculate_semantic_similarity(
    resume_text,
    jd_text
)
save_json(
    result,
    "data/resumes/processed_resumes/semantic_match.json"
)

print("=" * 50)
print("SEMANTIC MATCH RESULT")
print("=" * 50)
print(result)