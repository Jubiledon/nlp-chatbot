from intent_handlers.question_answering_handler import QuestionAnsweringHandler
from intent_handlers.discoverability_handler import DiscoverabilityHandler
from intent_handlers.identity_handler import IdentityHandler
from intent_handlers.small_talk_handler import SmallTalkHandler
from intent_handlers.travel_booking_handler import TravelBookingHandler

INTENT_REGISTRY = {
    "small_talk": SmallTalkHandler(),
    "discoverability": DiscoverabilityHandler(),
    "identity": IdentityHandler(),
    "question_answering": QuestionAnsweringHandler(),
    "travel_booking": TravelBookingHandler(),
}