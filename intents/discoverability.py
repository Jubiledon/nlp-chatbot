import random
from core.intent_handler import IntentHandler

DISCOVERABILITY_ANSWERS = [
    "I can chat with you, help with questions, and remember some things.",
    "I’m here to talk with you, help you learn, and answer simple queries.",
    "I can answer questions, have conversations, and help however I can."
]

class DiscoverabilityHandler(IntentHandler):
    def handle(self, user_input, context, sub_intent=None):
        print(random.choice(DISCOVERABILITY_ANSWERS))
