import json
import Pyro5.api
import Pyro5.errors

class Server:
    def __init__(self) -> None:
        # We create a proxy with a PYRONAME uri.
        # That allows Pyro to look up the object again in the NS when
        # it needs to reconnect later.
        self.__server = Pyro5.api.Proxy("PYRONAME:server.router")
        pass
    
    def exec(self, method, url, payload):
        response = self.__server.exec(method, url, payload)
        return json.loads(response)
