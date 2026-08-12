from ats_engine.normalization import normalize_text
from ats_engine.bias_reduction import mask_personal_information
from ats_engine.score_normalizer import normalize_score

resume = {
    "name": "Muhammed Sahal",
    "email": "sahalmuhammedsahalca@gmail.com",
    "phone": "+91 8138809977",
    "skills": "Python, SQL, Power BI!!"
}

print("=" * 50)
print("NORMALIZED TEXT")
print("=" * 50)
print(normalize_text(resume["skills"]))

print()

print("=" * 50)
print("MASKED DATA")
print("=" * 50)
print(mask_personal_information(resume))

print()

print("=" * 50)
print("NORMALIZED SCORE")
print("=" * 50)
print(normalize_score(88.824))