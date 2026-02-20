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
        typeMessage = messages['type']
        print(messages)
        text =  util.GetTextUser(messages)
        print(f"Received message: {text} from number: {number}")
        GenerateMessage(text, number,typeMessage)
        return "EVENT_RECEIVED", 200

    except Exception as e:
        print(e)
        return "ERROR_RECEPTION", 400

def GenerateMessage(text, number,typeMessage):
    if "text" in typeMessage:
        data = util.TextMessage(text, number)
    if "format" in typeMessage:        
        data = util.TextMessageFormat(number)
    if "image" in typeMessage:
        data = util.ImageMessage(number)
    if "audio" in typeMessage:
        data = util.AudioMessage(number)
    if "document" in typeMessage:
        data = util.DocumentMessage(number)
    if "video" in typeMessage:
        data = util.VideoMessage(number)
    if "location" in typeMessage:
        data = util.LocationMessage(number)
    if 'button' in typeMessage:
        data = util.ButtonsMessage(number)
    whatsappservice.sendMessageWhatsapp(data)
    
if __name__ == '__main__':
    app.run(debug=True)