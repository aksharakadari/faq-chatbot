from flask import Flask, request, jsonify
from flask_cors import CORS
from faq_data import faq_data  # Import FAQ data

# ✅ Define the Flask app before using @app.route()
app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/api/faq", methods=["GET"])
def get_answer():
    question = request.args.get("question", "").lower().strip()  # Convert to lowercase & remove extra spaces
    answer = faq_data.get(question, "Sorry, I don't have an answer for that.")
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)