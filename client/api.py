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

    def __send(self, msg):
        
        self.__sock.send(msg.encode())

        # espera sempre um json em formato de string do servidor
        response = self.__sock.recv(4096)

        return json.loads(response.decode())

    def GET(self, url):
        self.__start_connection()

        header = {
            "method": "GET",
            "content_type": "text",
        }

        header_response = self.__send(json.dumps(header))

        if header_response['status'] == 500:
            self.__end_connection()
            return header_response

        message = 'GET;' + url

        response = self.__send(message)

        self.__end_connection()
        
        return response

    def POST(self, url, dictionary):
        self.__start_connection()

        data = json.dumps(dictionary)

        header = {
            "method": "POST",
            "content_type": "json",
            "size": len(data)
        }

        # enviar header com pre-conteudo para server
        header_response = self.__send(json.dumps(header))

        if header_response['status'] == 500:
            self.__end_connection()
            return header_response

        # enviar conteudo com url
        message = 'POST;' + url + ';' + data

        # espera resposta do servidor para o cliente
        response = self.__send(message)

        self.__end_connection()

        return response
    
    def UPLOAD(self, file):
        filePath = os.getcwd() + '/client/assets/Logo.png'
        fileSize = os.path.getsize(filePath)
        
        self.__start_connection()

        header = {
            "method": "POST",
            "content_type": "file",
            "size": fileSize
        }

        # enviar header com pre-conteudo para server
        header_response = self.__send(json.dumps(header))

        if header_response['status'] == 500:
            self.__end_connection()
            return header_response
        
        payload = {
            'file_name': 'Logo.png'
        }

        message = 'POST;' + '/upload' + ';' + json.dumps(payload)

        # espera resposta do servidor para o cliente
        messageResponse = self.__send(message)

        with open(filePath, 'rb') as f:
            while True:
                bytes_read = f.read(4096)
                print('sending bytes', len(bytes_read))
                if not bytes_read:
                    break
                self.__sock.sendall(bytes_read)

        fileResponseBuff = self.__sock.recv(4096)
        
        fileResponse = json.loads(fileResponseBuff.decode())

        response = self.__send('EOF')

        print(response)

        self.__end_connection()

        return response
