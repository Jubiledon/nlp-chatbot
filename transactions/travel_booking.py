from data.travel_booking.slot_schema import TRAVEL_SLOT_SCHEMA
from transactions.transaction_session import TransactionSession

TRAVEL_SLOTS = [slot["name"] for slot in TRAVEL_SLOT_SCHEMA]

class TravelBookingSession(TransactionSession):
    def __init__(self):
        super().__init__(TRAVEL_SLOTS)
