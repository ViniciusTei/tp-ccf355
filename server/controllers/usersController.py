import json

from router import STATUS
from models import usersModel
from error import Error

def GetUsers():
    users = usersModel.getAllUsers()
    games = gameModel.getAllGames()

    response = {
        "users": users,
        "status": STATUS['SUCCESS']
    }

    # todas as respostas devem estar formatadas em string
    # para poder ser enviada para o client no metodo send
    return json.dumps(response)


def CreateUser(payload):
    user = usersModel.createUser(username=payload['username'], password=payload['password'], image=payload['image'])

    if user:
        response = {
            "user": user,
            "status": STATUS['SUCCESS']
        }
    else:
        response = Error(message='Erro ao criar usuario', status=500)

    return json.dumps(response)

def UpdateUser(payload):
    user = usersModel.updateUser(iduser=payload['iduser'], image=payload['image'])

    if user:
        response = {
            "user": user,
            "status": STATUS['SUCCESS']
        }
    else:
        response = Error(message='Erro ao criar usuario', status=500)

    return json.dumps(response)