from flask import Flask, request, jsonify

app = Flask(__name__)

def shogik_reply(text):
    text = text.lower()

    if "բարև" in text:
        return "Բարև 😊 ես Շողիկն եմ"
    elif "ինչ ես անում" in text:
        return "Ես խոսում եմ քեզ հետ 🤖"
    elif "ինչ ես" in text:
        return "Ես պարզ AI եմ 🤖"
    else:
        return "Չհասկացա 😅"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")
    return jsonify({"reply": shogik_reply(msg)})

@app.route("/")
def home():
    return "Shogik AI is running..."

app.run(host="0.0.0.0", port=5000)
