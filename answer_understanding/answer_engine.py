from answer_understanding.intent_classifier import classify_intent
from answer_understanding.entity_extractor import extract_entities
from answer_understanding.response_validator import validate_answer
from answer_understanding.semantic_formatter import format_semantic

def analyze_answer(answer):

    intent = classify_intent(answer)
    entities = extract_entities(answer)
    status = validate_answer(answer)

    return format_semantic(intent, entities, status)