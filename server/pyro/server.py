import Pyro5.server

from routes import Router

class PyroService(object):
    @Pyro5.server.expose
    def Router(self, method, url, payload):
        return Router.run(method=method, url=url, payload=payload)