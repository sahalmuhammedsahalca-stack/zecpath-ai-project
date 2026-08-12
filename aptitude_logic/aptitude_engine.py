from aptitude_logic.reasoning_questions import QUESTIONS
from aptitude_logic.scenario_generator import get_scenario
from aptitude_logic.answer_mapper import ideal_answer
from aptitude_logic.logic_scoring import score
from aptitude_logic.clarity_detector import clarity

def evaluate(answer):

    return {
        "question": QUESTIONS[0],
        "scenario": get_scenario(),
        "ideal_answer": ideal_answer(),
        "logic_score": score(answer),
        "clarity": clarity(answer)
    }