from flask import Flask, request
import os 
from dotenv import load_dotenv
import util
import whatsappservice

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
        print(f"Received token: {token}, challenge: {challenge}, expected token: {accessToken}")
        if token and challenge and token == accessToken:
            return challenge
        else:
            return "Error, wrong token!", 400
            
    except Exception as e:
        print(e)
        return "Error en verificación", 400

@app.route('/whatsapp', methods=["POST"])
def ReceivedMessage():
    try:
        body = request.get_json() 
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        messages = (value['messages'])[0]
        number = messages['from']
        print(messages)
        text =  util.GetTextUser(messages)
        print(f"Received message: {text} from number: {number}")
        GenerateMessage(text, number)
        return "EVENT_RECEIVED", 200

    except:
        return "ERROR_RECEPTION", 400

def GenerateMessage(text, number):
    text = 'The user said: ' + text
    whatsappservice.sendMessageWhatsapp(text, number)
    
if __name__ == '__main__':
    app.run(debug=True)