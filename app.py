# career-finder/app.py
from flask import Flask, render_template, send_from_directory
from career_data import CAREERS

# It's good practice to initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main single-page application."""
    # Pass the entire CAREERS dictionary from your career_data.py to the template
    return render_template('index.html', careers_data=CAREERS)

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serves static files (CSS, JS, images)."""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # For local development, debug=True is fine.
    # For production, use a proper WSGI server like Gunicorn or Waitress.
    app.run(debug=True)
