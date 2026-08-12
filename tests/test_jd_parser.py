from parsers.jd_parser import parse_job_description
from parsers.json_writer import save_json

# Read Job Description
with open(
    "data/job_descriptions/raw_job_descriptions/data_analyst_jd.txt",
    "r",
    encoding="utf-8"
) as file:
    jd_text = file.read()

# Parse Job Description
job_data = parse_job_description(jd_text)

# Save JSON
output_path = "data/job_descriptions/sample_jd.json"
save_json(job_data, output_path)

print("=" * 50)
print("JOB DESCRIPTION PARSER OUTPUT")
print("=" * 50)
print(job_data)