INTENT_EXAMPLES = [
    # ---- Start travel booking ----
    ("i want to book a flight", "travel_booking", "start"),
    ("book a flight for me", "travel_booking", "start"),
    ("i need to book a trip", "travel_booking", "start"),
    ("help me book a flight", "travel_booking", "start"),
    ("i want to book a plane ticket", "travel_booking", "start"),
    ("can you help me travel", "travel_booking", "start"),

    # ---- Provide travel information ----
    ("from london", "travel_booking", "provide_info"),
    ("to paris", "travel_booking", "provide_info"),
    ("i am travelling from manchester", "travel_booking", "provide_info"),
    ("i want to go to berlin", "travel_booking", "provide_info"),
    ("return trip", "travel_booking", "provide_info"),
    ("one way", "travel_booking", "provide_info"),
    ("10/11/2025", "travel_booking", "provide_info"),
    ("20/11/2025", "travel_booking", "provide_info"),
    ("i am flexible with dates", "travel_booking", "provide_info"),

    # ---- Confirmation ----
    ("yes confirm", "travel_booking", "confirm"),
    ("that is correct", "travel_booking", "confirm"),
    ("confirm booking", "travel_booking", "confirm"),
    ("yes that works", "travel_booking", "confirm"),

    # ---- Change details ----
    ("change the return date", "travel_booking", "change"),
    ("i want to change something", "travel_booking", "change"),
    ("change my booking", "travel_booking", "change"),
    ("modify the trip", "travel_booking", "change"),

    # ---- Cancellation ----
    ("cancel the booking", "travel_booking", "cancel"),
    ("never mind", "travel_booking", "cancel"),
    ("stop booking", "travel_booking", "cancel"),
]
