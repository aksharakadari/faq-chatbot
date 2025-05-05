from flask import Flask, request, jsonify
from faq_data import faq_answers
app = Flask(__name__)

# Sample FAQ database
faq_answers = {
    "What is AI?": "AI stands for Artificial Intelligence, which enables machines to simulate human-like decision-making.",
    "How does Flask work?": "Flask is a lightweight web framework for Python, used to build APIs and web applications.",
    "What is Python?": "Python is a high-level programming language used for web development, data science, and automation."
}

@app.route('/faq', methods=['GET'])
def faq():
    question = request.args.get('q', '').strip()  # Ensure clean input
    answer = faq_answers.get(question, "I don't have an answer for that yet.")
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)