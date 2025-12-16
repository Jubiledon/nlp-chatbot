import re
from core.chat_context import ChatContext
from core.intent_handler import IntentHandler
from core.similarity import find_best_match

SET_NAME_PREFIXES = [
    "my name is",
    "i am called",
    "call me",
]

class IdentityHandler(IntentHandler):
    def handle(self, user_input, context, sub_intent):
        new_name, reply = handle_identity(user_input, context, sub_intent)
        context.user_name = new_name
        print(reply)

# Handles identity-related intents: setting and getting the user's name.
# Returns (new_user_name_or_old, reply_string)
def handle_identity(user_input, context: ChatContext, sub_intent):
    user_input_lower = user_input.lower().strip()
    if sub_intent == "set_name": return handle_set_name(user_input_lower, context)
    if sub_intent == "get_name": return handle_get_name(context)
    return context.user_name, "Could you tell me your name?"

def handle_set_name(user_input_lower, context):
    extracted_name = extract_user_name_from_input(user_input_lower)
    if extracted_name:
        return extracted_name, f"Nice to meet you, {extracted_name}!"
    else:
        return context.user_name, "I didn't catch your name — could you repeat it?"
    
def handle_get_name(context):
    if context.user_name:
        return context.user_name, f"Your name is {context.user_name}."
    else:
        return context.user_name, "I don’t know your name yet."

# Extracts a name from user input using fuzzy prefix matching.
# Handles spelling mistakes like 'my nam is james'.
def extract_user_name_from_input(text):
    prefix = find_name_prefix(text)
    if not prefix:
        return None
    candidate = extract_name_candidate(text, prefix)
    if not candidate:
        return None
    return normalize_name(candidate)

# Decide whether the user is trying to set a name, and which prefix they meant.
def find_name_prefix(text):
    idx, score = find_best_match(text, SET_NAME_PREFIXES)
    if score < 0.4:
        return None
    return SET_NAME_PREFIXES[idx]

# Pull out what might be the name, without caring if it’s valid.
def extract_name_candidate(text, prefix):
    remainder = text[len(prefix):].strip()
    if not remainder:
        return None
    return remainder.split()[0]

# Turn a name like "j@mes!!" into "James"
def normalize_name(token):
    cleaned = "".join(
        c for c in token
        if c.isalpha() or c in ("-", "'")
    )
    return cleaned.capitalize() if cleaned else None