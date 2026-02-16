from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome', methods=["GET"])
def index():
    return "Welcome developer!"

@app.route('/whatsapp', methods=["GET"])
def VerifyToken():
    return "token verify!"

@app.route('/whatsapp', methods=["POST"])
def ReceivedMessage():
    return "received message!"

if __name__ == '__main__':
    app.run(debug=True)