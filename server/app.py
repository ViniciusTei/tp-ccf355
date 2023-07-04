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

@app.get("/lobby")
def lobbies():
    res = make_response(lobbyController.GetAllLobbies())
    return res

@app.post("/lobby")
def createLobby():
    payload = request.json
    res = make_response(lobbyController.CreateLobby(payload))
    return res

@app.get("/lobby-by-id")
def lobbyById(id):
    payload = {
        "lobbyid": id
    }
    res = make_response(lobbyController.GetLobbyById(payload))
    return res

@app.post("/lobby-leave")
def leaveLobby():
    payload = request.json
    res = make_response(lobbyController.LeaveLobby(payload))
    return res

@app.post("/lobby-enter")
def enterLobby():
    payload = request.json
    res = make_response(lobbyController.EnterLobby(payload))
    return res

@app.post("/check-for-challenges")
def checkFormChallenges():
    payload = request.json
    res = make_response(matchController.CheckForLobbies(payload))
    return res

@app.post("/lobby-by-page")
def lobbyByPage():
    payload = request.json
    res = make_response(lobbyController.GetAllLobbies(payload))
    return res

@app.get("/games")
def games():
    res = make_response(gamesController.GetAllGames())
    return res

@app.post("/match")
def createMatch():
    payload = request.json
    res = make_response(matchController.Create(payload))
    return res

@app.post("/match-by-id")
def matchById():
    payload = request.json
    res = make_response(matchController.GetMatch(payload))
    return res

@app.post("/challenges")
def challenges():
    payload = request.json
    res = make_response(matchController.GetAllChallenges(payload))
    return res

@app.post("/accept-challenge")
def acceptChallenge():
    payload = request.json
    res = make_response(matchController.AcceptChallenge(payload))
    return res

@app.post("/reject-challenge")
def rejectChallenge():
    payload = request.json
    res = make_response(matchController.RejectChallenge(payload))
    return res

if __name__ == '__main__':
    app.run()