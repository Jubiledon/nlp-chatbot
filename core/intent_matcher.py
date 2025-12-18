from data.intent_examples import INTENT_EXAMPLES
from core.similarity import find_best_match

#
# Matches user input to the best intent based on predefined example phrases.
#
def match_intent_and_subintent(user_input, context):
    phrases = [p for p, _, _ in INTENT_EXAMPLES]
    labels = [(intent, sub) for _, intent, sub in INTENT_EXAMPLES]
    intent_index, score = find_best_match(user_input, phrases)
    intent, sub_intent = labels[intent_index]
    return intent, sub_intent, score


