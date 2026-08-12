from ats_engine.ranking_engine import rank_candidates
from ats_engine.shortlisting import shortlist_candidate
from utils.json_writer import save_json

# Sample candidates
candidates = [
    {"name": "Muhammed Sahal", "final_score": 88.82},
    {"name": "John", "final_score": 92.50},
    {"name": "Alice", "final_score": 78.40},
    {"name": "David", "final_score": 65.30}
]

# Rank candidates
ranked_candidates = rank_candidates(candidates)
# Add shortlist status
for candidate in ranked_candidates:
    candidate["status"] = shortlist_candidate(candidate["final_score"])

# Save ranked candidates
save_json(
    ranked_candidates,
    "data/resumes/processed_resumes/ranked_candidates.json"
)

print("=" * 60)
print("RANKED CANDIDATES")
print("=" * 60)

for rank, candidate in enumerate(ranked_candidates, start=1):

    print(f"Rank #{rank}")
    print(f"Name   : {candidate['name']}")
    print(f"Score  : {candidate['final_score']}")
    print(f"Status : {candidate['status']}")
    print("-" * 60)