def GetTextUser(message):
    text = ""
    typeMessage = message["type"]
    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactive = message["interactive"]
        typeInteractive = interactive["type"]
        if typeInteractive == "button_reply":
            text = (interactive["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactive["list_reply"])["title"]
        else:
            print("[!] Interactive type not supported")
    else:
        print("[!] Message type not supported")
    return text

def TextMessage(textUser, number):
    data = {
                    "messaging_product": "whatsapp",    
                    "recipient_type": "individual",
                    "to": number,
                    "type": "text",
                    "text": {
                        "preview_url": False,
                        "body": textUser
                    }
                }
    return data

def TextMessageFormat(number):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": "*Hola* Bernardo _Todo bien_"
        }
    }
    return data

def ImageMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": number,
        "type": "image",
        "image": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/image_whatsapp.png"
        }
    }
    return data

def AudioMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": number,
        "type": "audio",
        "audio": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3"
        }
    }
    return data

def VideoMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": number,
        "type": "video",
        "video": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4"
        }
    }
    return data

def DocumentMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": number,
        "type": "document",
        "document": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf"
        }
    }
    return data

def LocationMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": number,
        "type": "location",
        "location": {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "name": "San Francisco",
            "address": "San Francisco, CA"
        }
    }
    return data

def ButtonsMessage(number):
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "¿Qué deseas hacer?"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "button1",
                            "title": "Ver productos"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "button2",
                            "title": "Ver servicios"
                        }
                    }
                ]
            }
        }
    }
       
    return data