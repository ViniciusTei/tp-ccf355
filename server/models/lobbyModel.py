from db import database
from models import usersModel

def getAllLobbies():
    databaseConn = database.DB().db

    lobbiesTupleList = databaseConn.execute('SELECT idlobby, name, username, image FROM lobby AS l JOIN lobby_has_user AS lhu ON l.idlobby=lhu.lobby_idlobby JOIN user AS u ON u.iduser = lhu.user_iduser').fetchall()
    
    databaseConn.close()

    lobbiesList = []
    
    for lobby in lobbiesTupleList:
        if not any(d['lobbyid'] == lobby[0] for d in lobbiesList):
            # does not exist
            lobbiesList.append({
                "lobbyid": lobby[0],
                "lobbyname": lobby[1],
                "users": [{
                    "username": lobby[2],
                    "userimage": lobby[3]
                }]
            })
        else:
            for l in lobbiesList:
                if l['lobbyid'] == lobby[0]:
                    l['users'].append({
                        "username": lobby[2],
                        "userimage": lobby[3]
                    })
    
    return lobbiesList
    
def getLobbyById(id):
    databaseConn = database.DB().db

    lobbiesTupleList = databaseConn.execute('SELECT idlobby, name, username, image FROM lobby AS l JOIN lobby_has_user AS lhu ON l.idlobby=lhu.lobby_idlobby JOIN user AS u ON u.iduser = lhu.user_iduser WHERE l.idlobby=?', (id,)).fetchall()
    
    databaseConn.close()

    lobbyDict = {}
    lobbyDict['lobbyid'] = lobbiesTupleList[0][0] 
    lobbyDict['lobbyname'] = lobbiesTupleList[0][1]
    lobbyDict['users'] = []

    for lobby in lobbiesTupleList:
        print(lobby[2])
        lobbyDict['users'].append({
            "username": lobby[2],
            "userimage": lobby[3]
        })

    return lobbyDict

def getLobbiesByName(name):
    databaseConn = database.DB().db

    lobbiesTupleList = databaseConn.execute('SELECT * FROM lobby WHERE name = ?', (name,)).fetchone()
    print(lobbiesTupleList)
    
    databaseConn.close()

    lobbyDict = {}

    lobbyDict['id'] = lobbiesTupleList[0] 
    lobbyDict['name'] = lobbiesTupleList[1]
    lobbyDict['game'] = lobbiesTupleList[2]
    
    return lobbyDict

def createLobby(userId, gameId):
    user = usersModel.getUserById(userId)

    name = 'TIME_' + user['username']

    databaseConn = database.DB().db
    cursor = databaseConn.execute('INSERT INTO lobby (name,game_idgame) VALUES (?, ?)', (name, gameId,))
    idlobby = cursor.lastrowid
    # adicionar o criador da lobby nela
    databaseConn.execute('INSERT INTO lobby_has_user (lobby_idlobby, user_iduser) VALUES (?, ?) ', (idlobby, userId))
    databaseConn.commit()

    return {
            'lobbyId': idlobby,
            'lobbyName': name
        }

def enterLobby(lobbyid, userid):
    databaseConn = database.DB().db
    cursor = databaseConn.execute('SELECT idlobby, count(iduser) FROM lobby AS l JOIN lobby_has_user AS lhu ON l.idlobby=lhu.lobby_idlobby JOIN user AS u ON u.iduser = lhu.user_iduser WHERE l.idlobby=? GROUP by l.idlobby', (lobbyid,))
    responseTuple = cursor.fetchone()
    count = responseTuple[1]

    if count >= 5:
        return {
            'message': 'Lobby full!'
        }
    
    databaseConn.execute('INSERT INTO lobby_has_user (lobby_idlobby, user_iduser) VALUES (?, ?) ', (lobbyid, userid))
    databaseConn.commit()

    return {
        'message': 'Success!'
    }