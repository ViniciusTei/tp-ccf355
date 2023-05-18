from db import database

def getAllUsers():
    databaseConn = database.DB().db

    usersTupleList = databaseConn.execute('SELECT * FROM user').fetchall()
    
    databaseConn.close()

    usersList = []

    for user in usersTupleList:
        usersList.append({
             "id": user[0],
             "username": user[1],
             "password": user[2]
        })

    return usersList