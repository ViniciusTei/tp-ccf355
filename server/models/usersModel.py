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

def createUser(username, password, image):
    databaseConn = database.DB().db

    cursor = databaseConn.execute('INSERT INTO user (username,password,image) VALUES (?, ?, ?)', (username, password, image,))
    iduser = cursor.lastrowid
    databaseConn.commit()

    if iduser == None:
        return None
    else:
        return {
            'id': iduser,
            'username': username,
            'image': image
        }

def getUserById(id):
    databaseConn = database.DB().db

    usersTupleList = databaseConn.execute('SELECT * FROM user WHERE iduser = ?', (id,)).fetchone()
    
    databaseConn.close()

    userDict = {}

    userDict['id'] = usersTupleList[0] 
    userDict['username'] = usersTupleList[1]
    userDict['image'] = usersTupleList[3]
    return userDict

def updateUser(iduser, username, password , image):
    databaseConn = database.DB().db

    databaseConn.execute('UPDATE user SET image = ? WHERE iduser = ?', (image, iduser,))
    databaseConn.commit()

    if iduser == None:
        return None
    else:
        return {
            'id': iduser,
            'image': image
        }