import socket

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
    
    if (dataSplitted[1] == '/user'):
        connection.send('User connected! Vinicius'.encode())
    else:
        connection.send('Route not found!'.encode())