from speech_processing.stt_service import speech_to_text
from speech_processing.text_cleaner import clean_text
from speech_processing.silence_detector import detect_silence
from speech_processing.speech_handler import handle_partial_answer


def process_transcript(audio):

    transcript = speech_to_text(audio)

    if detect_silence(transcript):
        return {
            "status": "Silence Detected"
        }

    cleaned = clean_text(transcript)

    return {
        "transcript": cleaned,
        "answer_status": handle_partial_answer(cleaned)
    }