import json

from router import STATUS
from models import usersModel, lobbyModel

def PostSession(payload):
    users = usersModel.getAllUsers()

    response = {
        'message': 'User incorrect!',
        'status': STATUS['NOTFOUND']
    }

    for user in users:
        if user['username'] == payload['username'] and user['password'] == payload['password']:
            response['user'] = user
            response['message'] = 'User connected! %s'%(payload['username'])
            response['status'] = STATUS['SUCCESS']
    
    return json.dumps(response)