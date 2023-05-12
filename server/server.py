import socket
import json
from routes import Router

s = socket.socket()

port = 4000

s.bind(('', port))
s.listen(5)

routes = ['/user']

print('Server running on port 4000!')
while True:
    connection, addr = s.accept()
    # connection.send('Connected to server in port 4000'.encode())
    print("Accepted a connection request from %s:%s"%(addr[0], addr[1]))
    data = connection.recv(1024).decode()
    dataSplitted = data.split(';')

    payload = None

    if(dataSplitted[2]):
        payload = json.loads(dataSplitted[2])

    response = Router.run(dataSplitted[0], dataSplitted[1], payload)

    connection.send(response.encode())
    
    # if (dataSplitted[1] == '/session'):
    #     payload = json.loads(dataSplitted[2])
    #     print('Received from server', payload)

    #     if (payload['password'] == '123'):
    #         response = 'User connected! %s'%(payload['username'])
    #         connection.send(response.encode())
    #     else:
    #         connection.send('User incorrect!'.encode())
    # else:
    #     connection.send('Route not found!'.encode())