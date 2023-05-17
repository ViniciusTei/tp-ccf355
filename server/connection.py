import json
from _thread import *
import os

from routes import Router

MAX_BUFF_SIZE = 4096

class Connection:
  def __init__(self, conn) -> None:
    self.__connection = conn
    pass

  def start(self):
    start_new_thread(self.__handle_connection, (self.__connection, ))

  def __handle_request(self, connection):
    # recebe do cliente um header com dados da requisicao
    headersBuff = connection.recv(MAX_BUFF_SIZE).decode()
    headers = json.loads(headersBuff)
    print("Request headers", headers)

    contentType = headers['content_type']

    headersResponse = dict()

    if contentType not in ['file', 'json', 'text']:
          headersResponse = {
              'message': 'Content not permited!',
              'status': 500
          }
          connection.send(json.dumps(headersResponse).encode())
          connection.close()
          return
    else:
          headersResponse = {
              'message': 'Headers received!',
              'status': 200
          }
          connection.send(json.dumps(headersResponse).encode())

    payload = None

    data = connection.recv(MAX_BUFF_SIZE).decode()
    dataSplitted = data.split(';')

    if contentType == 'file':
          connection.send(json.dumps({ 'message': 'Ready to receive file!' }).encode())

          payload = json.loads(dataSplitted[2])

          buff = b''
          while True:
              buff_read = connection.recv(MAX_BUFF_SIZE)
              print("received buff size",len(buff_read))
              if len(buff_read) < MAX_BUFF_SIZE:
                  buff += buff_read
                  break
              buff += buff_read

          connection.send(json.dumps({ 'message': 'File received!' }).encode())

          EOF = connection.recv(MAX_BUFF_SIZE).decode()
          
          if EOF == 'EOF':
              filePath = os.getcwd() + '/server/temp/' + payload['file_name']
              f = open(filePath, 'wb')
              f.write(buff)
              f.close()

    elif contentType == 'json':
          payload = json.loads(dataSplitted[2])

    return (dataSplitted[0], dataSplitted[1], payload)

  def __handle_connection(self, connection):

    (method, url, payload) = self.__handle_request(connection)

    # espera uma resposta em string para enviar para o cliente
    # a string deve ser sempre um json parseado para string
    response = Router.run(method=method, url=url, payload=payload)

    connection.send(response.encode())

    connection.close()