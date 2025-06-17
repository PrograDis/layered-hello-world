"""
Business Logic Layer.
Contains application-specific rules and logic.
"""

from data.hello_repository import fetch_hello_message

def get_processed_message():
    """
    Retrieves the base message from the data layer
    and applies business logic (e.g., formatting).
    """
    base_message = fetch_hello_message()
    return base_message.upper()  # Example of business logic
