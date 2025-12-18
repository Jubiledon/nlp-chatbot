from core.similarity import find_best_match
from core.intent_handler import IntentHandler

class QuestionAnsweringHandler(IntentHandler):
    def handle(self, user_input, context, sub_intent=None):
        idx, score = find_best_match(user_input, context.questions)
        if score < 0.25:
            print("I'm not sure about that one. Can you ask something else?")
        else:
            print(context.answers[idx])
