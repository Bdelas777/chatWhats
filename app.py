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
        GenerateMessage(messages, text, number, typeMessage)
        return "EVENT_RECEIVED", 200

    except Exception as e:
        print(e)
        return "ERROR_RECEPTION", 400

def GenerateMessage(messages, text, number, typeMessage):
    # Default reply
    data = util.TextMessage("Lo siento, no entendí tu mensaje.", number)

    try:
        if typeMessage == "text":
            t = (text or "").strip().lower()
            if t in ["hola", "hi", "hello"] or "hola" in t:
                data = util.TextMessage("¡Hola! ¿Deseas ver productos o servicios?", number)
            else:
                # Echo back by default
                data = util.TextMessage(f"Recibí: {text}", number)

        elif typeMessage == "interactive":
            interactive = messages.get("interactive", {})
            itype = interactive.get("type")
            if itype == "button_reply":
                title = interactive.get("button_reply", {}).get("title", "")
                if title.lower() == "ver productos":
                    data = util.ListMessage(number)
                elif title.lower() == "ver servicios":
                    data = util.TextMessage("Nuestros servicios:\n- Servicio X\n- Servicio Y\n- Servicio Z", number)
                else:
                    data = util.TextMessage(f"Has pulsado: {title}", number)

            elif itype == "list_reply":
                title = interactive.get("list_reply", {}).get("title", "")
                # Productos
                if title in ["Producto A", "Producto B", "Producto C"]:
                    data = util.TextMessage(f"Detalle de {title}: Aquí tienes la descripción y precio.", number)
                elif title in ["Servicio X", "Servicio Y", "Servicio Z"]:
                    data = util.TextMessage(f"Detalle de {title}: Información del servicio.", number)
                else:
                    data = util.TextMessage(f"Seleccionaste: {title}", number)

        else:
            # Other media types: send a friendly confirmation
            data = util.TextMessage("Mensaje recibido. ¿Quieres probar con 'hola' o ver opciones?", number)

    except Exception as e:
        print(f"Error generating message: {e}")
        data = util.TextMessage("Ocurrió un error procesando tu mensaje.", number)

    whatsappservice.sendMessageWhatsapp(data)
    
if __name__ == '__main__':
    app.run(debug=True)