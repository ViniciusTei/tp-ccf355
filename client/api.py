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

        response = self.sock.recv(1024)
        
        self.sock.close()

        return response

    def GET(self, url):
        message = 'GET;' + url

        response = self.__send(message)

        return response.decode()

    def POST(self, url, dictionary):
        data = json.dumps(dictionary) 
        message = 'POST;' + url + ';' + data

        response = self.__send(message)

        return response.decode()
