from speech_processing.transcript_processor import process_transcript
from speech_processing.stt_tester import TEST_CASES

print("=" * 60)
print("SPEECH TO TEXT TEST")
print("=" * 60)

for test in TEST_CASES:

    result = process_transcript(test)

    print(result)