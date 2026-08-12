from conversation_flow.conversation_engine import process_answer
from conversation_flow.sample_inputs import ANSWERS

print("=" * 60)
print("AI CONVERSATION FLOW")
print("=" * 60)

for answer in ANSWERS:
    print(process_answer(answer))