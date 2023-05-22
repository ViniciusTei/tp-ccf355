import json

from router import STATUS
from models import lobbyModel
from error import Error

def GetAllLobbies():
    lobbies = lobbyModel.getAllLobbies()

    response = {
        "lobbies": lobbies,
        "status": STATUS['SUCCESS']
    }

    # todas as respostas devem estar formatadas em string
    # para poder ser enviada para o client no metodo send
    return json.dumps(response)


def CreateLobby(payload):
    lobby = lobbyModel.createLobby(username=payload['userId'], password=payload['gameId'])

    if lobby:
        response = {
            "lobbyName": lobby['name'],
            "status": STATUS['SUCCESS']
        }
    else:
        response = Error(message='Erro ao criar lobby', status=500)

    return json.dumps(response)