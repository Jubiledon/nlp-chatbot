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
        self.active_transaction = None  # e.g. "travel_booking", "store_ordering"
        self.transaction_session = None  # e.g. session data for the active transaction

    def start_transaction(self, transaction_name, session):
            self.active_transaction = transaction_name
            self.transaction_session = session

    def end_transaction(self):
        self.active_transaction = None
        self.transaction_session = None

    def has_active_transaction(self):
        return self.transaction_session is not None

    def has_user_name(self):
        return self.user_name is not None