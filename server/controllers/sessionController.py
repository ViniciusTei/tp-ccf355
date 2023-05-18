import json

from router import STATUS
from models import usersModel
from models import gameModel

def PostSession(payload):
    users = usersModel.getAllUsers()
    games = gameModel.getAllGames()
    gamers= gameModel.getGameById(1)

    response = {
        'message': 'User incorrect!',
        'status': STATUS['NOTFOUND']
    }

    for user in users:
        if user['username'] == payload['username'] and user['password'] == payload['password']:
            response['message'] = 'User connected! %s'%(payload['username'])
            response['status'] = STATUS['SUCCESS']
    
    return json.dumps(response)