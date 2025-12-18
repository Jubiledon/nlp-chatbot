from utils.date_utils import format_date

TRAVEL_SLOT_SCHEMA = [
    {
        "name": "origin",
        "label": "From",
        "required": True,
        "formatter": None,
        "condition": None,
    },
    {
        "name": "destination",
        "label": "To",
        "required": True,
        "formatter": None,
        "condition": None,
    },
    {
        "name": "trip_type",
        "label": "Trip type",
        "required": True,
        "formatter": lambda v: v.replace("_", " ").title(),
        "condition": None,
    },
    {
        "name": "departure_date",
        "label": "Departure date",
        "required": True,
        "formatter": format_date,
        "condition": None,
    },
    {
        "name": "return_date",
        "label": "Return date",
        "required": False,
        "formatter": format_date,
        "condition": lambda s: s.get_slot("trip_type") == "return",
    },
    {
        "name": "num_of_tickets",
        "label": "Number of tickets",
        "required": True,
        "formatter": None,
        "condition": None,
    },
]
