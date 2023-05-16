import socket
import json

PORT = 4000

class API:
    def __init__(self, sock=None) -> None:
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        pass
    
    def __connect(self, host, port):
        self.sock.connect((host, port))

    def __send(self, msg):
        self.__connect('localhost', PORT)
        
        self.sock.send(msg.encode())

        # espera sempre um json em formato de string do servidor
        response = self.sock.recv(4096)
        
        self.sock.close()

        return json.loads(response.decode())

    def GET(self, url):

        # header = {
        #     "method": "GET",
        # }

        message = 'GET;' + url

        response = self.__send(message)

        return response

    def POST(self, url, dictionary):
        data = json.dumps(dictionary)

        # header = {
        #     "method": "POST",
        #     "content_type": "json",
        #     "size": len(data)
        # }

        # enviar header com pre-conteudo para serer

        # enviar conteudo com url
        message = 'POST;' + url + ';' + data

        # espera resposta do servidor para o cliente
        response = self.__send(message)

        return response
    
    # def UPLOAD(self, file, fileSize):
        
    #     header = {
    #         "method": "POST",
    #         "content_type": "file",
    #         "size": fileSize
    #     }
