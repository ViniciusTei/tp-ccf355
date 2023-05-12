import socket

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

    def GET(self, url):
        message = 'GET;' + url

        self.__connect('localhost', PORT)
        
        self.sock.send(message.encode())

        response = self.sock.recv(1024)
        
        self.sock.close()

        return response.decode()
