from intents.question_answering import QuestionAnsweringHandler
from intents.discoverability import DiscoverabilityHandler
from intents.identity import IdentityHandler
from intents.small_talk import SmallTalkHandler

INTENT_REGISTRY = {
    "small_talk": SmallTalkHandler(),
    "discoverability": DiscoverabilityHandler(),
    "identity": IdentityHandler(),
    "question_answering": QuestionAnsweringHandler(),
}