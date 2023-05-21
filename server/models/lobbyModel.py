from db import database
from models import usersModel

def getAllLobbies():
    databaseConn = database.DB().db

    lobbiesTupleList = databaseConn.execute('SELECT * FROM lobby AS l JOIN lobby_has_user AS lhu ON l.idlobby=lhu.lobby_idlobby JOIN user AS u ON u.iduser = lhu.user_iduser').fetchall()
    
    databaseConn.close()

    lobbiesList = []
    

    for lobby in lobbiesTupleList:
        print(lobby)
        lobbiesList.append({
             "lobbyid": lobby[0],
             "lobbyname": lobby[1],
             "gameid": lobby[2],
             "iduser": lobby[5],
             "username": lobby[6],
        })
    
    

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

    cursor = databaseConn.execute('INSERT INTO lobby (name,game_idgame) VALUES (?, ?)', (name, gameId,))
    idlobby = cursor.lastrowid
    print(idlobby)
    databaseConn.commit()

    return {
            'lobbyId': idlobby,
            'lobbyName': name
        }
