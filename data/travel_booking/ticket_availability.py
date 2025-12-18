# Ticket availability between supported cities
# Format:
# AVAILABILITY[origin][destination] = number_of_tickets

TICKET_AVAILABILITY = {
    "London": {
        "Paris": 12,
        "Berlin": 5,
        "New York": 3,
        "Manchester": 20,
        "Nottingham": 15,
        "Tokyo": 2,
    },
    "Paris": {
        "London": 10,
        "Berlin": 8,
        "New York": 4,
        "Tokyo": 3,
    },
    "Berlin": {
        "London": 6,
        "Paris": 7,
        "Manchester": 5,
        "Tokyo": 2,
    },
    "New York": {
        "London": 4,
        "Paris": 3,
        "Los Angeles": 18,
        "Tokyo": 6,
    },
    "Manchester": {
        "London": 22,
        "Nottingham": 25,
        "Paris": 6,
    },
    "Nottingham": {
        "London": 14,
        "Manchester": 20,
    },
    "Los Angeles": {
        "New York": 16,
        "Tokyo": 7,
        "London": 3,
    },
    "Tokyo": {
        "London": 2,
        "Paris": 3,
        "New York": 5,
        "Los Angeles": 6,
    },
}
