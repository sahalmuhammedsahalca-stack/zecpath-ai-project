from optimization.resume_cleaner import clean_resume
from optimization.performance_timer import measure_time
from optimization.entity_optimizer import normalize_skill

sample_text = """
Python      SQL

Power BI

Excel!!!!!!
"""

print("=" * 50)
print("RESUME CLEANER")
print("=" * 50)

cleaned = clean_resume(sample_text)
print(cleaned)

print()

print("=" * 50)
print("ENTITY NORMALIZATION")
print("=" * 50)

print(normalize_skill("python"))
print(normalize_skill("sql"))
print(normalize_skill("power bi"))

print()

print("=" * 50)
print("PERFORMANCE")
print("=" * 50)

result = measure_time(clean_resume, sample_text)

print("Execution Time:", result["execution_time"], "seconds")
print("Cleaned Text:", result["result"])

from optimization.false_result_handler import reduce_false_results
from optimization.followup_stability import stabilize_followup
from optimization.scoring_optimizer import (
    normalize_score,
    detect_scoring_anomaly
)
from optimization.transcript_optimizer import clean_transcript
from optimization.performance_optimizer import measure_processing_time


print()
print("=" * 50)
print("DAY 42 - STABILITY OPTIMIZATION")
print("=" * 50)

print()
print("FALSE RESULT HANDLING")
print("Score 85:", reduce_false_results(85))
print("Score 65:", reduce_false_results(65))

print()
print("FOLLOW-UP STABILITY")
print(stabilize_followup("Tell me about yourself.", ""))
print(
    stabilize_followup(
        "Tell me about yourself.",
        "I have two years of experience."
    )
)

print()
print("SCORING OPTIMIZATION")
print("Valid:", normalize_score(88.829))
print("Negative:", normalize_score(-10))
print("High:", normalize_score(150))
print("Anomaly Check:", detect_scoring_anomaly(88))

print()
print("TRANSCRIPT OPTIMIZATION")

raw_text = "um my name is Sahal uh I have two years of experience"

print("Raw:", raw_text)
print("Cleaned:", clean_transcript(raw_text))

print()
print("PERFORMANCE OPTIMIZATION")

performance = measure_processing_time(
    clean_transcript,
    raw_text
)

print(
    "Processing Time:",
    performance["processing_time_seconds"],
    "seconds"
)

print("=" * 50)