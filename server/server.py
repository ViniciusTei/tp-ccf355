import socket

from connection import Connection

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 4000

    s.bind(('', port))
    s.listen(5)

    print('Server running on port 4000!')

    try:
        while True:
            connection, addr = s.accept()

            print("Accepted a connection request from %s:%s"%(addr[0], addr[1]))

            newConnection = Connection(connection)

            newConnection.start()
            
    except KeyboardInterrupt:
        s.close()
        print("Interruption server.")
    finally:
        exit 
    
    s.close()