from db import database
from models import usersModel

def getAllLobbies():
    databaseConn = database.DB().db

    lobbiesTupleList = databaseConn.execute('SELECT * FROM lobby AS l ').fetchall()
    
    databaseConn.close()

    lobbiesList = []
    print(lobbiesTupleList)

    for lobby in lobbiesTupleList:
        lobbiesList.append({
             "id": lobby[0],
             "name": lobby[1]
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

    cursor = databaseConn.execute('INSERT INTO lobby (name,game_idgame) VALUES (?, ?)', (name, gameId,))
    idlobby = cursor.lastrowid
    print(idlobby)
    databaseConn.commit()

    return {
            'lobbyId': idlobby,
            'lobbyName': name
        }
