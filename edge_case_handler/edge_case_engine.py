from edge_case_handler.audio_checker import check_audio
from edge_case_handler.language_detector import detect_language
from edge_case_handler.missing_answer_handler import handle_missing
from edge_case_handler.retry_engine import retry
from edge_case_handler.safety_fallback import fallback


def evaluate(audio, text):

    if check_audio(audio) == "Retry":
        return retry(fallback())

    if handle_missing(text) == "Missing":
        return retry("Answer not detected.")

    if detect_language(text) == "Mixed":
        return "Mixed language detected."

    return "Response accepted."