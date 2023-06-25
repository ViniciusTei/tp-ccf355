from flask import Flask, request, make_response, jsonify
from controllers import sessionController, usersController, lobbyController, gamesController, matchController

app = Flask(__name__)

@app.route("/users", methods=['GET', 'POST'])
def users():
    if(request.method == 'GET'):
        return usersController.GetUsers()
    else:
       payload = request.json
       return usersController.CreateUser(payload)
    
@app.route("/session", methods=['POST'])
def session():
    payload = request.json
    return sessionController.PostSession(payload)

if __name__ == '__main__':
    app.run()