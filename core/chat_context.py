#
# A simple class to hold the chat context, including user name,
# loaded questions and answers for question answering.
# Works as a single shared state model for the chatbot.
#
class ChatContext:
    def __init__(self, questions, answers):
        self.user_name = None
        self.questions = questions
        self.answers = answers