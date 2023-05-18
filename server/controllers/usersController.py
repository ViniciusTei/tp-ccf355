import json

from router import STATUS
from models import usersModel
from models import gameModel


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