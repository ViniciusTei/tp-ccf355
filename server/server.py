import socket
import json
from _thread import *

from routes import Router

def handle_connection(connection):
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

if __name__ == '__main__':
    numThreads = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 4000

    s.bind(('', port))
    s.listen(5)

    print('Server running on port 4000!')

    try:
        while True:
            connection, addr = s.accept()

            print("Accepted a connection request from %s:%s"%(addr[0], addr[1]))
            
            start_new_thread(handle_connection, (connection, ))
            numThreads += 1
    except KeyboardInterrupt:
        print("Interruption server.")
    finally:
        exit 
    
    s.close()