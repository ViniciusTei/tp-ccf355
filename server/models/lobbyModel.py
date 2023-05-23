from db import database
from models import usersModel

def getAllLobbies():
    databaseConn = database.DB().db

    lobbiesTupleList = databaseConn.execute('SELECT * FROM lobby AS l JOIN lobby_has_user AS lhu ON l.idlobby=lhu.lobby_idlobby JOIN user AS u ON u.iduser = lhu.user_iduser ORDER BY l.idlobby').fetchall()
    
    databaseConn.close()

    lobbiesList = []
    print(lobbiesTupleList)
    

    for lobby in lobbiesTupleList:
        print(lobby)
        lobbiesList.append({
             "lobbyid": lobby[0],
             "lobbyname": lobby[1],
             "gameid": lobby[2],
             "iduser": lobby[5],
             "username": lobby[6],
        })
    return lobbiesList
    

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
    print(user)
    name = 'TIME_' + user['username']
    print(name)

    databaseConn = database.DB().db

    cursor = databaseConn.execute('INSERT INTO lobby (name,gameid) VALUES (?, ?)', (name, gameId,))
    idlobby = cursor.lastrowid
    print(idlobby)
    databaseConn.commit()
    databaseConn.close()
    lobbyhasuser = joinLobby(idlobby, userId)
    print(lobbyhasuser)
    return {
            'lobbyId': idlobby,
            'lobbyName': name,
            'userId': lobbyhasuser['userId']
        }

def joinLobby(lobbyId, userId):
    databaseConn = database.DB().db

    databaseConn.execute('INSERT INTO lobby_has_user (lobby_idlobby,user_iduser) VALUES (?, ?)', (lobbyId, userId,))
    databaseConn.commit()
    databaseConn.close()
    return {
            'userId': userId
        }

def exitLobby(lobbyId, userId):
    databaseConn = database.DB().db

    databaseConn.execute('DELETE FROM lobby_has_user WHERE lobby_idlobby = ? AND user_iduser = ?', (lobbyId, userId,))
    databaseConn.commit()
    databaseConn.close()

def deleteLobby(lobbyId):
    databaseConn = database.DB().db

    databaseConn.execute('DELETE FROM lobby AS l WHERE idlobby = ?', (lobbyId,))
    databaseConn.commit()
    databaseConn.close()

