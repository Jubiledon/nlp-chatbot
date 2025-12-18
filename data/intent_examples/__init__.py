from .small_talk import INTENT_EXAMPLES as SMALL_TALK
from .identity import INTENT_EXAMPLES as IDENTITY
from .discoverability import INTENT_EXAMPLES as DISCOVERABILITY
from .question_answering import INTENT_EXAMPLES as QUESTION_ANSWERING
from .travel_booking import INTENT_EXAMPLES as TRAVEL_BOOKING

INTENT_EXAMPLES = (
    SMALL_TALK
    + IDENTITY
    + DISCOVERABILITY
    + QUESTION_ANSWERING
    + TRAVEL_BOOKING
)
