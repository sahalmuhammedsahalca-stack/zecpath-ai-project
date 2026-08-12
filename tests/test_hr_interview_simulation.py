from hr_interview_simulation.candidate_profiles import CANDIDATES
from hr_interview_simulation.simulation_engine import run_simulation


print("=" * 60)
print("HR INTERVIEW SIMULATION")
print("=" * 60)

results = run_simulation(CANDIDATES)

for result in results:
    print(result)