from eligibility_engine.ats_connector import get_candidate
from eligibility_engine.decision_engine import generate_decision
from eligibility_engine.result_formatter import format_result

candidate = get_candidate()

result = generate_decision(candidate)

format_result(result)