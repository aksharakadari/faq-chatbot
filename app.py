from flask import Flask, render_template, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)      # Define your Flask app first.
CORS(app)                  # Now call CORS with the defined app.

# Define your routes below:
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq', methods=['GET'])
def faq():
    question = request.args.get('q', '').strip()
    # Use your logic here. For example:
    answer = "This is a sample answer. Replace this with your actual logic."
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)