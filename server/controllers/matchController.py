import json

from router import STATUS
from models import matchModel
from error import Error

def Create(payload):
    response = matchModel.createMatch(payload['requester'], payload['challenge'])

    if (hasattr(response, 'error')):
        return Error(response['error'], STATUS['ERROR']).toString()
    else:
        response['status'] =  STATUS['SUCCESS']
        return json.dumps(response)
    
def GetAllChallenges(payload):
    response = matchModel.getChallenges(payload['lobbyid'])

    if (hasattr(response, 'error')):
        return Error(response['error'], STATUS['ERROR']).toString()
    else:
        response['status'] =  STATUS['SUCCESS']
        return json.dumps(response)