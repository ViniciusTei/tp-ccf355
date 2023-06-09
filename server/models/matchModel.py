import sqlite3

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
    databaseConn.close()
    response = {
        'message': 'Desafio criado com sucesso!'
    }

    return response
    
def getChallenges(lobbyId):
    databaseConn = database.DB().db
    cursor = databaseConn.execute('SELECT idlobby, name, situation FROM match_challenge JOIN lobby ON match_challenge.lobby_requester=lobby.idlobby WHERE match_challenge.lobby_challenged == ?', (lobbyId,))
    allLobbies = cursor.fetchall()
    lobbiesList = []

    for l in allLobbies:
        if (l[2] == 'P'):
            lobbiesList.append({
                'lobbyid': l[0],
                'name': l[1],
            })

    response = {
        'message': 'Sucesso!',
        'lobbies': lobbiesList
    }

    databaseConn.close()
    
    return response

def accept(lobbyId, requesterLobbyId):
    databaseConn = database.DB().db

    try:
        cursor = databaseConn.execute('SELECT match_callenge_id, match_id FROM match_challenge WHERE match_challenge.lobby_challenged == ? AND WHERE match_challenge.lobby_requester = ?', (lobbyId,requesterLobbyId))
        lobby = cursor.fetchone()
        cursor = databaseConn.execute('UPDATE match_challenge SET situation=? WHERE match_challenge.match_callenge_id=?', ('A', lobby[0]))
        databaseConn.commit()
        databaseConn.close()

        return {
            'message': 'Sucesso!',
            'match': lobby[1]
        }
    
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        databaseConn.close()
        
        return {
            'message': 'Erro!',
            'error': ' '.join(er.args)
        }
    
def reject(lobbyId, requesterLobbyId):
    databaseConn = database.DB().db

    try:
        cursor = databaseConn.execute('SELECT match_callenge_id FROM match_challenge WHERE match_challenge.lobby_challenged == ? AND WHERE match_challenge.lobby_requester = ?', (lobbyId,requesterLobbyId))
        lobby = cursor.fetchone()
        cursor = databaseConn.execute('UPDATE match_challenge SET situation=? WHERE match_challenge.match_callenge_id=?', ('R', lobby[0]))
        databaseConn.commit()
        databaseConn.close()

        return {
            'message': 'Sucesso!'
        }
    
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        databaseConn.close()
        
        return {
            'message': 'Erro!',
            'error': ' '.join(er.args)
        }