from flask import Flask, request, jsonify
from langdetect import detect
from deep_translator import GoogleTranslator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/detect_translate', methods=['POST'])
def detect_translate():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    try:
        detected_lang = detect(text)
        translated_text = GoogleTranslator(source=detected_lang, target='en').translate(text)

        return jsonify({
            "detected_language": detected_lang,
            "translated_text": translated_text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)



# Hola, ¿cómo estás? Estoy aprendiendo desarrollo web.

# मुझे अंग्रेजी सीखना है और मैं प्रतिदिन अभ्यास कर रही हूँ।
