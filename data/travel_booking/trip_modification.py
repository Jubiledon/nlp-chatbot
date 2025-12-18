MODIFICATION_PHRASES = {
    "origin": [
        "change origin",
        "modify origin",
        "update origin",
        "change departure city",
        "update departure location",
        "i want to leave from somewhere else",
        "can i change where i’m leaving from",
        "from"
    ],
    "destination": [
        "change destination",
        "modify destination",
        "update destination",
        "change arrival city",
        "update arrival location",
        "i want to go somewhere else",
        "can i change where i’m going",
    ],
    "trip_type": [
        "change trip type",
        "modify trip type",
        "update trip type",
        "make it a return trip",
        "make it one way",
        "switch to round trip",
        "i want a one-way ticket instead",
    ],
    "departure_date": [
        "change departure date",
        "modify departure date",
        "update departure date",
        "leave a day later",
        "leave earlier",
        "can i change the departure day",
        "move the departure date",
    ],
    "return_date": [
        "change return date",
        "modify return date",
        "update return date",
        "come back later",
        "return earlier",
        "can i change the return day",
        "move the return date",
    ],
    "num_of_tickets": [
        "change number of tickets",
        "modify number of tickets",
        "update number of tickets",
        "add more tickets",
        "remove a ticket",
        "i need more seats",
        "reduce the number of tickets",
    ],
}

def flatten_modification_phrases():
    return [
        phrase
        for phrases in MODIFICATION_PHRASES.values()
        for phrase in phrases
    ]

ALL_MODIFICATION_PHRASES = flatten_modification_phrases()
