import random
from core.intent_handler import IntentHandler

DISCOVERABILITY_ANSWERS = [
    "I can chat with you, help you book a trip, answer questions, and remember some things! What would you like to know?",
]

class DiscoverabilityHandler(IntentHandler):
    def handle(self, user_input, context, sub_intent=None):
        print(random.choice(DISCOVERABILITY_ANSWERS))
