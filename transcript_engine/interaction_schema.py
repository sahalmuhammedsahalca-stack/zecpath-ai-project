from transcript_engine.metadata import create_metadata
from transcript_engine.normalizer import normalize_transcript


def create_interaction(question, answer):

    metadata = create_metadata()

    return {
        **metadata,
        "question": question,
        "answer": normalize_transcript(answer)
    }