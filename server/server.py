import socket

s = socket.socket()

port = 4000

s.bind(('', port))
s.listen(5)

print('Server running on port 4000!')
while True:
    connection, addr = s.accept()
    connection.send('Connected to server in port 4000'.encode())
    print("Accepted a connection request from %s:%s"%(addr[0], addr[1]))
    data = connection.recv(1024).decode()
    print(data)