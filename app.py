from flask import Flask, request, jsonify
from langdetect import detect, detect_langs

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect_language():
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "Please provide 'text' in JSON body"}), 400

    text = data["text"]
    try:
        lang = detect(text)
        probs = detect_langs(text)
        return jsonify({"detected_language": lang, "probabilities": [str(p) for p in probs]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
