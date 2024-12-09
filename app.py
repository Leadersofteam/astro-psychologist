from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")

    # Prosta odpowiedź Astrologa-Psychologa
    response = {
        "message": f"Cześć! Jestem Twoim Astrologiem-Psychologiem. Słyszałem, że masz pytanie: {user_message}. Oto moja odpowiedź!"
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)