from core.intent_matcher import match_intent_and_subintent
from core.qa_loader import load_qa_dataset
from core.intent_registry import INTENT_REGISTRY
from core.chat_context import ChatContext

# Program entry point
def main():
    print("Hello! I'm your chatbot. Type 'exit' to quit.")
    questions, answers = load_qa_dataset("data/COMP3074-CW1-Dataset.csv")
    context = ChatContext(questions,answers)
    start_chatbot_loop(context)

# =========================
# Helper functions
# ========================

def start_chatbot_loop(context):
    while True:
        user_input = input("> ")
        if does_user_want_to_exit(user_input):
            handle_user_exit()
            break
        match_and_handle_intent(user_input, context)

def match_and_handle_intent(user_input, context):
    intent, sub_intent, score = match_intent_and_subintent(user_input)
    intent_handler = INTENT_REGISTRY.get(intent)
    if not intent_handler or score < 0.2:
        print("Sorry, I didn’t quite get that.")
        return
    intent_handler.handle(user_input, context, sub_intent)

def does_user_want_to_exit(user_input):
    if user_input.lower() in ["exit", "quit"]:
        return True
    return False

def handle_user_exit():
    print("Goodbye! Have a great day!")

if __name__ == "__main__":
    main()