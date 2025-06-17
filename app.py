"""
Application entry point.
Initializes the Flask app and registers routes from the presentation layer.
"""

from flask import Flask
from presentation.hello_view import register_routes

# Create Flask app instance
app = Flask(__name__)

# Register presentation routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
