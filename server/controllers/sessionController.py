import json

from router import STATUS

users = [
        {
            "id": 0,
            "username": "vinicius",
            "password": "123"
        }
    ]

def PostSession(payload):
    response = {
        'message': 'User incorrect!',
        'status': STATUS['NOTFOUND']
    }

    for user in users:
        if user['username'] == payload['username'] and user['password'] == payload['password']:
            response['message'] = 'User connected! %s'%(payload['username'])
            response['status'] = STATUS['SUCCESS']
    
    return json.dumps(response)