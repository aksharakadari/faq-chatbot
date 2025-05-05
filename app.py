from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS module
import os  # Import os for environment variables
from faq_data import faq_data  # Import the dictionary directly

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin requests

@app.route('/')
def home():
    return "Welcome to my chatbot!"

@app.route('/faq', methods=['GET'])
def get_answer():
    # Retrieve the question from the query string parameter "q"
    question = request.args.get('q')
    
    # Optionally, return an error if no question is provided
    if not question:
        return jsonify({'error': 'Please provide a question using the "q" parameter.'}), 400

    # Use the dictionary's .get() method to find the answer or return a default message
    answer = faq_data.get(question, "Sorry, I don't have an answer for that.")
    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    # Use PORT from environment variables if available, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)