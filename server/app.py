from flask import Flask, request, make_response, jsonify
from controllers import sessionController, usersController, lobbyController, gamesController, matchController

app = Flask(__name__)

@app.route("/users", methods=['GET', 'POST'])
def users():
    if(request.method == 'GET'):
        res = make_response(usersController.GetUsers())
        return res
    else:
       payload = request.json
       res = make_response(usersController.CreateUser(payload))
       return res
    
@app.route("/session", methods=['POST'])
def session():
    payload = request.json
    res = make_response(sessionController.PostSession(payload))
    return res

if __name__ == '__main__':
    app.run()