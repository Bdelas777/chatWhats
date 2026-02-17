import requests
import json
import os 
from dotenv import load_dotenv

def sendMessageWhatsapp(textUser ,number):
    try:
        token = os.getenv("VERIFY_TOKEN_APP")
        api_url = "https://graph.facebook.com/v22.0/1043923432128675/messages"
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
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("Message sent successfully")
            return True
        
        print(f"Failed to send message: {response.status_code} - {response.text}")
        return False
    except Exception as e:
        print(f"Error sending message: {e}")
        return False