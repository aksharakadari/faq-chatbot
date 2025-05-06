from flask import Flask, render_template, jsonify, request
from faq_data import faq_answers

app = Flask(__name__)

@app.route('/')
def home():
    # This will serve the index.html template located inside the templates folder
    return render_template('index.html')

@app.route('/faq', methods=['GET'])
def faq():
    question = request.args.get('q', '').strip()
    answer = faq_answers.get(question, "I don't have an answer for that yet.")
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)