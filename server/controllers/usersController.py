import json

from router import STATUS
from models import usersModel

def GetUsers():
    users = usersModel.getAllUsers()

    response = {
        "users": users,
        "status": STATUS['SUCCESS']
    }

    # todas as respostas devem estar formatadas em string
    # para poder ser enviada para o client no metodo send
    return json.dumps(response)