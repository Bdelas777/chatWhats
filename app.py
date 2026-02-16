from flask import Flask, request
import os 
from dotenv import load_dotenv
app = Flask(__name__)

@app.route('/welcome', methods=["GET"])
def index():
    return "Welcome developer!"

@app.route('/whatsapp', methods=["GET"])
def VerifyToken():
    try:
        accessToken = os.getenv("VERIFY_TOKEN")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        if token and challenge and token == accessToken:
            return challenge
        else:
            return "Error, wrong token!", 400
            
    except Exception as e:
        print(e)
        return "Error en verificación", 400

@app.route('/whatsapp', methods=["POST"])
def ReceivedMessage():
    return "received message!"

if __name__ == '__main__':
    app.run(debug=True)