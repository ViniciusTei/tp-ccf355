import json

from models import gameModel
from router import STATUS

def GetAllGames():
    games = gameModel.getAllGames()

    response = {
        'games': games,
        'status': STATUS['NOTFOUND']
    }

    return json.dumps(response)