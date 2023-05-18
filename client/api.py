import socket
import json
import os

PORT = 4000

class API:
    def __init__(self, sock=None) -> None:
        if sock is None:
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.__sock = sock
        pass
    
    def __start_connection(self):
        self.__sock.connect(('localhost', PORT))
    
    def __end_connection(self):
        self.__sock.close()

    def __send(self, msg, headers):
        responseData = dict()
        
        self.__start_connection()
        
        self.__sock.send(json.dumps(headers).encode())

        header_response_bytes = self.__sock.recv(4096)
        
        header_response = json.loads(header_response_bytes.decode())

        if header_response['status'] == 500:
            self.__end_connection()
            return  header_response
        
        self.__sock.send(msg.encode())

        # espera sempre um json em formato de string do servidor
        response = self.__sock.recv(4096)

        try:
            responseData = json.loads(response.decode())
        except ValueError as e:
            responseData['status'] = 500
            responseData['message'] = 'Resposta invalida do servidor! Precisa ser uma JSON string!'

        self.__end_connection()
        
        return responseData


    def GET(self, url):
        header = {
            "method": "GET",
            "content_type": "text",
        }

        message = 'GET;' + url

        response = self.__send(message, headers=header)
        
        return response

    def POST(self, url, dictionary):
        data = json.dumps(dictionary)

        header = {
            "method": "POST",
            "content_type": "json",
            "size": len(data)
        }

        # enviar conteudo com url
        message = 'POST;' + url + ';' + data

        # espera resposta do servidor para o cliente
        response = self.__send(message, headers=header)

        return response
    
    # def UPLOAD(self, file):
    #     filePath = os.getcwd() + '/client/assets/Logo.png'
    #     fileSize = os.path.getsize(filePath)

    #     header = {
    #         "method": "POST",
    #         "content_type": "file",
    #         "size": fileSize
    #     }

    #     # enviar header com pre-conteudo para server
    #     header_response = self.__send(json.dumps(header))

    #     if header_response['status'] == 500:
    #         self.__end_connection()
    #         return header_response
        
    #     payload = {
    #         'file_name': 'Logo.png'
    #     }

    #     message = 'POST;' + '/upload' + ';' + json.dumps(payload)

    #     # espera resposta do servidor para o cliente
    #     messageResponse = self.__send(message)

    #     with open(filePath, 'rb') as f:
    #         while True:
    #             bytes_read = f.read(4096)
    #             print('sending bytes', len(bytes_read))
    #             if not bytes_read:
    #                 break
    #             self.__sock.sendall(bytes_read)

    #     fileResponseBuff = self.__sock.recv(4096)
        
    #     fileResponse = json.loads(fileResponseBuff.decode())

    #     response = self.__send('EOF')

    #     print(response)

    #     self.__end_connection()

    #     return response
