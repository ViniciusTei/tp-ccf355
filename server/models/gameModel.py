from db import database

def getAllGames():
    databaseConn = database.DB().db

    gamesTupleList = databaseConn.execute('SELECT * FROM game').fetchall()
    
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

    gameTupleList = databaseConn.execute('SELECT * FROM game WHERE idgame = ?', (gameId,)).fetchone()
    
    databaseConn.close()

    gamesList = []

    gamesList.append({
        "id": gameTupleList[0],
        "name": gameTupleList[1]
    })

    print(gamesList)
    return gamesList
   