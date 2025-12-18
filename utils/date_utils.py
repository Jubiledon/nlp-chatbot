import re
from datetime import datetime

DATE_PATTERNS = [
    r"\b\d{2}/\d{2}/\d{4}\b",  # DD/MM/YYYY
    r"\b\d{2}-\d{2}-\d{4}\b",
]

# Extracts a date from text in DD/MM/YYYY or DD-MM-YYYY format.
# Returns a datetime object or None if no valid date is found.
def extract_date(text):
    for pattern in DATE_PATTERNS:
        match = re.search(pattern, text)
        if match:
            date_str = match.group()
            try:
                return datetime.strptime(date_str.replace("-", "/"), "%d/%m/%Y")
            except ValueError:
                return None
    return None

# Formats a datetime object into a string in DD/MM/YYYY format.
def format_date(date_obj):
    return date_obj.strftime("%d/%m/%Y")
