from db import database
from datetime import datetime

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

    databaseConn.execute('UPDATE user SET username = ?, password = ?, image = ? WHERE iduser = ?', (username, password, image, iduser,))
    databaseConn.commit()

    if iduser == None:
        return None
    else:
        return {
            'id': iduser,
            'image': image
        }
    
def createFriendRequisition(iduser1, iduser2):
    #Status = {Pending, Accept, Refused}
    now = datetime.utcnow()
    databaseConn = database.DB().db

    databaseConn.execute('INSERT INTO friend (user_iduser_1,user_iduser_2,start_date,update_date,status) VALUES (?, ?, ?, ?, ?)', (iduser1, iduser2, now, now, 'Pending',))
    databaseConn.commit()
    return{
        'iduser': iduser2
    }

def updateFriendRequest(iduser1, iduser2, status):
    friend = getFriendshipByIds(iduser1, iduser2)
    #Status = {Pending, Accept, Refused}
    now = datetime.utcnow()
    databaseConn = database.DB().db

    databaseConn.execute('UPDATE friend SET status = ?, update_date = ? WHERE user_iduser_1 = ? AND user_iduser_2 = ?', (status, now, iduser1, iduser2,))
    databaseConn.commit()


def getFriendshipByIds(iduser1, iduser2):
    databaseConn = database.DB().db

    usersTupleList = databaseConn.execute('SELECT * FROM friend WHERE user_iduser_1 = ? AND user_iduser_2 = ?', (iduser1, iduser2,)).fetchone()
    
    databaseConn.close()

    friendshipDict = {}

    friendshipDict['user_iduser_1'] = usersTupleList[0] 
    friendshipDict['user_iduser_2'] = usersTupleList[1]
    friendshipDict['start_date'] = usersTupleList[2]
    friendshipDict['update_date'] = usersTupleList[3]
    friendshipDict['status'] = usersTupleList[4]

    print(friendshipDict)
    return friendshipDict

def deleteFriendshipByIds(iduser1, iduser2):
    databaseConn = database.DB().db

    databaseConn.execute('DELETE FROM friend WHERE user_iduser_1 = ? AND user_iduser_2 = ?', (iduser1, iduser2,)).fetchone()
    
    databaseConn.commit()
