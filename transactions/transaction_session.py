from abc import ABC, abstractmethod

#
# Generic container for transactional dialogue state.
# Each transaction defines its own required slots and logic,
# but the session itself is generic and reusable.
#
class TransactionSession(ABC):
    def __init__(self, required_slots):
        self.required_slots = required_slots
        self.slots = {}
        self.confirmed = False
        self.pending_action = None  # e.g. "confirm_booking", "review_booking"

    def set_slot(self, slot_name, value):
        self.slots[slot_name] = value

    def has_slot(self, slot_name):
        return slot_name in self.slots

    def is_complete(self):
        return all(slot in self.slots for slot in self.required_slots)

    def missing_slots(self):
        return [s for s in self.required_slots if s not in self.slots]
    
    def get_next_missing_slot(self):
        for slot in self.required_slots:
            if not self.has_slot(slot):
                return slot
        return None

    def reset(self):
        self.slots = {}
        self.confirmed = False

    def reset_slot(self, slot_name):
        if slot_name in self.slots:
            del self.slots[slot_name]

    def get_slot(self, slot_name):
        return self.slots.get(slot_name, None)
