from summarization import Summarizer
from flask import Flask, request, jsonify


app = Flask(__name__)
summarizer = Summarizer()

# Flask endpoint for summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    text = data['text']
    summary = summarizer.summarize(text)
    # Take the first prediction
    output = {'summary': summary}
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)