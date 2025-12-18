from multiprocessing import context
from tokenize import String
from core.intent_handler import IntentHandler
from core.similarity import find_best_match
from data.travel_booking.supported_cities import CITIES
from data.travel_booking.trip_types import TRIP_TYPES
from data.travel_booking.slot_schema import TRAVEL_SLOT_SCHEMA
from transactions.travel_booking import TravelBookingSession
from utils.entity_extraction import extract_entity_from_text
from data.travel_booking.ticket_availability import TICKET_AVAILABILITY
from data.travel_booking.trip_modification import ALL_MODIFICATION_PHRASES
from data.travel_booking.trip_modification import MODIFICATION_PHRASES
from datetime import datetime

class TravelBookingHandler(IntentHandler):
    def handle(self, user_input, context, sub_intent):
        if not does_user_have_active_transaction(context):
            return handle_transaction_start(context)
        handle_transaction_input(user_input, context)
        
def does_user_have_active_transaction(context):
    return context.has_active_transaction()

# Handles if the user is starting a new travel booking transaction
def handle_transaction_start(context):
    context.start_transaction("travel_booking", TravelBookingSession())
    print(f"Let's start your travel booking {context.user_name if context.user_name != None else ' '}! First question: Which city are you travelling from?")
    print("These are the current cities we support:", ", ".join(CITIES))

def handle_transaction_input(user_input, context):
    if does_user_want_to_cancel(user_input): 
        return handle_transaction_cancellation(context)
    if not has_user_provided_all_info(context):
        return handle_slot_filling(user_input, context)
    if does_user_want_to_modify_booking(user_input):
        return handle_booking_modification(user_input, context)
    handle_booking_confirmation(user_input, context)

def does_user_want_to_modify_booking(user_input):
    idx, score = find_best_match(user_input, ALL_MODIFICATION_PHRASES)
    return score >= 0.4

def handle_booking_modification(user_input, context):
    session = context.transaction_session
    session.reset()
    print(f"Okay, let's update your booking. Please provide the new details:")
    print("Which city are you travelling from?")
    return

def handle_booking_confirmation(user_input, context):
    session = context.transaction_session
    confirmation_phrases = [
        "yes",
        "confirm",
        "sure",
        "absolutely"
    ]
    denial_phrases = [
        "no",
        "change",
        "modify",
        "edit"
    ]
    idx, confirm_score = find_best_match(user_input, confirmation_phrases)
    idx, deny_score = find_best_match(user_input, denial_phrases)
    if confirm_score > deny_score and confirm_score >= 0.4:
        print("Thank you! Your booking has been confirmed. A confirmation email will be sent to you shortly.")
        print("What would you like to do next?")
        context.end_transaction()
    elif deny_score > confirm_score and deny_score >= 0.4:
        print("Okay, let's update your booking. Would you like to enter the details again, or would you like to cancel altogether?")
    else:
        print("I didn't quite get that. Please respond with 'yes' to confirm or 'no' to modify your booking.")
    
def has_user_provided_all_info(context):
    session = context.transaction_session
    return session.is_complete()

def handle_slot_filling(user_input, context):
    session = context.transaction_session
    next_slot = session.get_next_missing_slot()
    fill_next_slot(next_slot, user_input, session)

def fill_next_slot(next_slot, user_input, session):
    match next_slot:
        case "origin": handle_origin(user_input, session)
        case "destination": handle_destination(user_input, session)
        case "trip_type": handle_trip_type(user_input, session)
        case "departure_date": handle_departure_date(user_input, session)
        case "return_date": handle_return_date(user_input, session)
        case "num_of_tickets": handle_num_of_tickets(user_input, session)

def handle_origin(user_input, session):
    city = extract_entity_from_text(user_input, CITIES)
    if city:
        session.set_slot("origin", city)
        print(f"Origin set to {city}. Where are you travelling to?")
    else:
        print("I didn't catch that. Please specify a valid origin city.")

def handle_destination(user_input, session):
    city = extract_entity_from_text(user_input, CITIES)
    if city:
        session.set_slot("destination", city)
        print(f"Destination set to {city}. What type of trip is this? (one-way/return)")
    else:
        print("I didn't catch that. Please specify a valid destination city.")

def handle_trip_type(user_input, session):
    trip_type = extract_entity_from_text(user_input, TRIP_TYPES)
    if trip_type:
        session.set_slot("trip_type", trip_type)
        print(f"Trip type set to {trip_type}.  Just a few more questions! When is your departure date? Please provide it in the format DD/MM/YYYY.")
    else:
        print("I didn't catch that. Please specify if this is a one-way or return trip.")

def handle_departure_date(user_input, session):
    parsed_date = datetime.strptime(user_input, "%d/%m/%Y").date()
    session.set_slot("departure_date", parsed_date)
    if parsed_date:
        session.set_slot("departure_date", parsed_date)
        if session.get_slot("trip_type") == "return":
            print("Departure date set. When is your return date? Please provide it in the format DD/MM/YYYY.")
        elif session.get_slot("trip_type") == "one-way":
            session.set_slot("return_date", datetime(9999,12,31).date())
            print("Departure date set. Checking available tickets...")
            check_available_tickets(session)
    else:
        print("I couldn't understand the date. Please provide a valid departure date.")

def handle_return_date(user_input, session):
    date = datetime.strptime(user_input, "%d/%m/%Y").date()
    if is_return_date_valid(date, session):
        session.set_slot("return_date", date)
        print("Return date set. Checking available tickets...")
        check_available_tickets(session)
    else:
        print("Please provide a return date that is after the departure date.")
    
def check_available_tickets(session):
    origin = session.get_slot("origin")
    destination = session.get_slot("destination")
    if origin in TICKET_AVAILABILITY and destination in TICKET_AVAILABILITY[origin]:
        available_tickets = TICKET_AVAILABILITY[origin][destination]
        print(f"There are {available_tickets} tickets available from {origin} to {destination}. How many would you like to book?")
    else:
        print("I'm afraid there are no tickets available for that route. Please consider other cities or wait for email updates on future availability.")
        session.reset_slot("origin")
        session.reset_slot("destination")

def is_return_date_valid(return_date, session):
    trip_type = session.get_slot("trip_type")
    if trip_type != "return":
        return True  
    if not return_date:
        print("Please provide a valid return date.")
        return False
    departure_date = session.get_slot("departure_date")
    if not departure_date:
        return True  # Departure date not set yet
    return return_date > departure_date

def does_user_want_to_cancel(user_input):
    cancellation_phrases = [
        "cancel my booking",
        "i want to cancel",
        "stop the booking",
        "abort the booking",
        "never mind"
    ]
    idx, score = find_best_match(user_input, cancellation_phrases)
    return score >= 0.4
    
def handle_transaction_cancellation(context):
    context.end_transaction()
    print("Your travel booking session has been cancelled. What would you like to do next?")

def handle_num_of_tickets(user_input, session):
    num_tickets = int(user_input)
    if num_tickets <= 0:
        print("Please provide a valid number of tickets (a positive integer).")
        return
    if num_tickets > TICKET_AVAILABILITY.get(session.get_slot("origin"), {}).get(session.get_slot("destination"), 0):
        print("Sorry, we don't have that many tickets available. Please choose a number between 1 and the available tickets.")
        return
    session.set_slot("num_of_tickets", num_tickets)
    print(f"Number of tickets set to {num_tickets}. Finally, please confirm your booking details:")
    confirm_booking(session)

def confirm_booking(session):
    print("Here are your booking details:")
    for slot in TRAVEL_SLOT_SCHEMA:
        slot_name = slot["name"]
        slot_value = session.get_slot(slot_name)
        formatter = slot["formatter"]
        if formatter and slot_value:
            slot_value = formatter(slot_value)
        print(f"{slot['label']}: {slot_value}")
    print("Do you confirm this booking? (yes/no)")

