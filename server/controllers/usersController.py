import json

from router import STATUS

users = [
        {
            "id": 0,
            "username": "vinicius",
            "password": "123"
        }
    ]

def GetUsers():
    response = {
        "users": users,
        "status": STATUS['SUCCESS']
    }

    # todas as respostas devem estar formatadas em string
    # para poder ser enviada para o client no metodo send
    return json.dumps(response)