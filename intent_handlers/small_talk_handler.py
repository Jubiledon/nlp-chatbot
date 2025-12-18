from core.intent_handler import IntentHandler
from core.chat_context import ChatContext
import random

SMALL_TALK_RESPONSES = {
    "greet": [
        "Hi there! What’s your name?",
        "Hello! Nice to see you. What's your name?",
        "Hey! What's your name?"
    ],

    "ask_wellbeing": [
        "I'm doing great, thanks! How about you?",
        "I'm good! Thanks for asking. How are you?",
        "Feeling awesome today — you?"
    ],

    "user_wellbeing_positive": [
        "That’s great to hear! What would you like to do today?",
    ],

    "user_wellbeing_negative": [
        "Ah, sorry to hear that. Hope things get better soon.",
        "That happens sometimes. I’m here if you need anything.",
        "Hope your day improves!"
    ],

    "polite_response": [
        "Nice to meet you too! What can I do for you today?",
        "Likewise! What can I help you with today?",
        "Pleasure meeting you! What can I do for you today?"
    ],

    "casual": [
        "Not much! What’s up with you?",
        "Just here to chat! What's on your mind?",
        "Same old, same old. What about you?"
    ],

    "fallback": [
        "Hey!",
        "Hello!",
        "Hi there!"
    ]
}


class SmallTalkHandler(IntentHandler):
    def handle(self, user_input, context, sub_intent=None):
        responses = SMALL_TALK_RESPONSES.get(sub_intent)
        if not responses:
            responses = SMALL_TALK_RESPONSES["fallback"]
        print(random.choice(responses))

