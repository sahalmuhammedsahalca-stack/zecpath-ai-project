def check_audio(audio_quality):

    if audio_quality.lower() == "poor":
        return "Retry"

    return "Clear"