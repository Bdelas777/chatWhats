import requests
import json
import os 
from dotenv import load_dotenv

def sendMessageWhatsapp(data):
    try:
        token = os.getenv("VERIFY_TOKEN_APP")
        print(token)
        api_url = "https://graph.facebook.com/v22.0/1043923432128675/messages"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.post(api_url,data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print("Message sent successfully")
            return True
        
        print(f"Failed to send message: {response.status_code} - {response.text}")
        return False
    except Exception as e:
        print(f"Error sending message: {e}")
        return False

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