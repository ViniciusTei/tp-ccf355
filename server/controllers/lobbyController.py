import json

from router import STATUS
from models import lobbyModel
from error import Error

def GetAllLobbies(payload):
    response = {}
    if (payload):
        lobbies, offset, total_pages = lobbyModel.getAllLobbiesWithPagination(offset=payload['page'])

        response = {
            "lobbies": lobbies,
            'current_page': offset,
            'total_pages': total_pages,
            "status": STATUS['SUCCESS']
        }
    else:
        lobbies = lobbyModel.getAllLobbies()

        response = {
            "lobbies": lobbies,
            "status": STATUS['SUCCESS']
        }

    # todas as respostas devem estar formatadas em string
    # para poder ser enviada para o client no metodo send
    return json.dumps(response)


def CreateLobby(payload):
    lobby = lobbyModel.createLobby(payload['userId'], payload['gameId'])

    if lobby:
        response = {
            "lobby": lobby,
            "status": STATUS['SUCCESS']
        }
    else:
        response = Error(message='Erro ao criar lobby', status=500)

    return json.dumps(response)

def GetLobbyById(payload):
    lobby = lobbyModel.getLobbyById(id=payload['lobbyid'])

    if lobby:
        response = {
            "lobby": lobby,
            "status": STATUS['SUCCESS']
        }
    else:
        response = Error(message='Erro ao criar lobby', status=500)

    return json.dumps(response)

def EnterLobby(payload):
    response = lobbyModel.enterLobby(lobbyid=payload['lobbyid'], userid=payload['userid'])

    if response['message'] == 'Success!':
        response['status'] = STATUS['SUCCESS']
        return json.dumps(response)
    else:
        return json.dumps(Error(message=response['message'], status=STATUS['ERROR']))
    
def LeaveLobby(payload):
    lobbyModel.LeaveLobby(lobbyid=payload['lobbyid'], userid=payload['userid'])
    response = {
        "message": "Ok",
        "status": STATUS['SUCCESS']
    }
    return json.dumps(response)