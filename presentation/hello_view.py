"""
Presentation Layer.
Handles HTTP requests and returns responses to the client.
"""

from flask import render_template_string
from business.hello_service import get_processed_message

def register_routes(app):
    """
    Registers routes with the Flask app.
    """
    @app.route("/")
    def index():
        """
        Main route that returns the processed Hello message.
        """
        message = get_processed_message()
        # Simple inline HTML to render the response
        return render_template_string("<h1>{{ message }}</h1>", message=message)
