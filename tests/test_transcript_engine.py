from transcript_engine.interaction_schema import create_interaction
from transcript_engine.transcript_exporter import export_transcript

interaction = create_interaction(
    "Tell me about yourself.",
    "  My name is Muhammed Sahal. I have two years of experience.   "
)

print("=" * 60)
print("VOICE TRANSCRIPT")
print("=" * 60)

for key, value in interaction.items():
    print(f"{key}: {value}")

print("=" * 60)

export_transcript(interaction)