from flask import Flask, request, jsonify, render_template
from faq_data import faq_data
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq', methods=['GET'])
def get_answer():
    question = request.args.get('q')
    answer = faq_data.faq_data.get(question, "Sorry, I don't have an answer for that.")
    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
from flask import Flask, request, jsonify
import faq_data  # Ensure faq_data.py is in the same folder as app.py

app = Flask(__name__)

# Home page with a welcome message.
@app.route('/')
def home():
    return "Welcome to my chatbot!"

# FAQ endpoint for handling questions via query parameter "q".
@app.route('/faq', methods=['GET'])
def get_answer():
    question = request.args.get('q')  # Get question from URL, e.g., ?q=What+is+AI?
    answer = faq_data.get(question, "Sorry, I don't have an answer for that.")
    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)

import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)