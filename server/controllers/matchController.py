import json

from router import STATUS
from models import matchModel
from error import Error

def Create(payload):
    response = matchModel.createMatch(payload['requester'], payload['challenge'])

    if (response['error']):
        return Error(response['error'], STATUS['ERROR']).toString()
    else:
        return json.dumps(response)