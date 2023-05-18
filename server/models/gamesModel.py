from db import database

def getAllGames():
    databaseConn = database.DB().db

    gamesTupleList = databaseConn.execute('SELECT * FROM games').fetchall()
    
    databaseConn.close()

    gamesList = []

    for game in gamesTupleList:
        gamesList.append({
             "id": game[0],
             "name": game[1]
        })
    print(gamesList)
    return gamesList

def getGameById(gameId):

    databaseConn = database.DB().db

    gamesTupleList = databaseConn.execute('SELECT * FROM games WHERE id = ? ', (gameId)).fetchall()
    
    databaseConn.close()

    gamesList = []

    for game in gamesTupleList:
        gamesList.append({
             "id": game[0],
             "name": game[1]
        })
    print(gamesList)
    return gamesList