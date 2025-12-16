from abc import ABC, abstractmethod
from core.chat_context import ChatContext

class IntentHandler(ABC):
    @abstractmethod
    def handle(self, user_input, context: ChatContext, sub_intent=None):
        pass