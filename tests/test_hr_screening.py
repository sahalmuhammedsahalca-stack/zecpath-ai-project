from hr_screening.conversation_builder import build_conversation
from hr_screening.dataset_exporter import export_dataset

conversation = build_conversation()

print("=" * 60)
print("HR SCREENING QUESTIONS")
print("=" * 60)

for item in conversation:
    print(item)

print("=" * 60)

export_dataset()

from hr_screening.language_config import SUPPORTED_LANGUAGES

print("\nSupported Languages")
print("===================")

for language in SUPPORTED_LANGUAGES:
    print(language)