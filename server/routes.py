import router
import json

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
        "status": router.STATUS['SUCCESS']
    }

    # todas as respostas devem estar formatadas em string
    # para poder ser enviada para o client no metodo send
    return json.dumps(response)

def PostSession(payload):
    response = {
        'message': 'User incorrect!',
        'status': router.STATUS['NOTFOUND']
    }

    for user in users:
        if user['username'] == payload['username'] and user['password'] == payload['password']:
            response['message'] = 'User connected! %s'%(payload['username'])
            response['status'] = router.STATUS['SUCCESS']
    
    return json.dumps(response)
            

Router = router.Router()

Router.get('/users', callback=GetUsers)
Router.post('/session', callback=PostSession)
