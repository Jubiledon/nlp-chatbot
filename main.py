from core.intent_matcher import match_intent_and_subintent
from core.qa_loader import load_qa_dataset
from core.intent_registry import INTENT_REGISTRY
from core.chat_context import ChatContext
import builtins
from utils.output import bot_print
from utils.user_utils import get_user_name

# Override the built-in print function to use bot_print
builtins._original_print = builtins.print
builtins.print = bot_print

# Program entry point
def main():
    print("Hello! I'm your chatbot. Type 'exit' to quit. How can I assist you today?")
    questions, answers = load_qa_dataset("data/COMP3074-CW1-Dataset.csv")
    context = ChatContext(questions,answers)
    start_chatbot_loop(context)

# =========================
# Helper functions
# ========================

def start_chatbot_loop(context):
    while True:
        user_input = input(f"{get_user_name(context)}: ")
        if does_user_want_to_exit(user_input):
            handle_user_exit()
            break
        dispatch_user_input(user_input, context)

def dispatch_user_input(user_input, context):
    intent_handler, sub_intent = resolve_intent_handler(user_input, context)
    if not intent_handler:
        print("Sorry, I didn’t quite get that. Could you please rephrase?")
        return
    intent_handler.handle(user_input, context, sub_intent)

# Active transactions take priority over intent matching
# If there's an active transaction, return its handler directly
# Else perform intent matching to find the appropriate handler
def resolve_intent_handler(user_input, context):
    if context.has_active_transaction():
        return get_active_transaction_handler(context), None
    return get_other_intent_handler_and_subintent(user_input, context)

def get_active_transaction_handler(context):
    if not context.has_active_transaction():
        return None
    return INTENT_REGISTRY.get(context.active_transaction)

def get_other_intent_handler_and_subintent(user_input, context):
    intent, sub_intent, score = match_intent_and_subintent(user_input, context)
    if score < 0.2:
        return None, None
    handler = INTENT_REGISTRY.get(intent)
    return handler, sub_intent

def does_user_want_to_exit(user_input):
    if user_input.lower() in ["exit", "quit"]:
        return True
    return False

def handle_user_exit():
    print("Goodbye! Have a great day!")

if __name__ == "__main__":
    main()