from db import database
from datetime import datetime

import models.lobbyModel as lobbyModel

def createMatch(requester_lobby_id, requested_lobby_id):
    response = {}
    databaseConn = database.DB().db

    # valida lobbys
    # uma lobby he valida se tem 5 jogadores e as duas tem o mesmo jogo
    lobby_requester = lobbyModel.getLobbyById(requester_lobby_id)
    lobby_requested = lobbyModel.getLobbyById(requested_lobby_id)

    if (len(lobby_requested['users']) < 5 or len(lobby_requester['users']) < 5):
        response = {
            'error': 'A lobby deve ter no minimo 5 jogadores!'
        }

        return response
    
    lobby_game_1 = lobbyModel.getLobbiesByName(lobby_requester['lobbyname'])['game']
    lobby_game_2 = lobbyModel.getLobbiesByName(lobby_requested['lobbyname'])['game']

    if (lobby_game_1 != lobby_game_2):
        response = {
            'error': 'As lobbies tem que ter o mesmo jogo!'
        }

        return response

    # cria partida
    cursor = databaseConn.execute('INSERT INTO `match` (start_date, end_date) VALUES (?, ?)', (datetime.now(),None))
    databaseConn.commit()
    idmatch = cursor.lastrowid

    cursor = databaseConn.execute('INSERT INTO match_challenge (match_id, lobby_requester, lobby_challenged, situation) VALUES (?, ?, ?, ?)', (idmatch, lobby_requester['lobbyid'], lobby_requested['lobbyid'], 'P' ))
    databaseConn.commit()
    
    response = {
        'message': 'Desafio criado com sucesso!'
    }

    return response
    