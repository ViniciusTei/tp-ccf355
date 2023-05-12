import socket
import json
from routes import Router

s = socket.socket()

port = 4000

s.bind(('', port))
s.listen(5)

print('Server running on port 4000!')
while True:
    connection, addr = s.accept()

    print("Accepted a connection request from %s:%s"%(addr[0], addr[1]))

    # recebe os dados do cliente, decodifica e splita
    data = connection.recv(1024).decode()
    dataSplitted = data.split(';')

    payload = None

    # cria um payload json se existente
    if(dataSplitted[2]):
        payload = json.loads(dataSplitted[2])

    # espera uma resposta em string para enviar para o cliente
    # a string deve ser sempre um json parseado para string
    response = Router.run(dataSplitted[0], dataSplitted[1], payload)

    connection.send(response.encode())

    connection.close()