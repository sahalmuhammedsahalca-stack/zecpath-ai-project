from candidate_ranking.ranking_engine import rank
from candidate_ranking.sample_candidates import CANDIDATES

print("=" * 60)
print("CANDIDATE RANKING ENGINE")
print("=" * 60)

results = rank(CANDIDATES)

for candidate in results:
    print(candidate)