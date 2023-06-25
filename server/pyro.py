from Pyro5.api import expose, Daemon, locate_ns
import Pyro5.errors

from routes import Router

@expose
class ServerRouter(object):
    def exec(self, method, url, payload):
        return Router.run(method, url, payload)

ns = locate_ns()

try:
    existing = ns.lookup("server.router")
    print("Object still exists in Name Server with id: %s" % existing.object)
    print("Previous daemon socket port: %d" % existing.port)
    # start the daemon on the previous port
    daemon = Daemon(port=existing.port)
    # register the object in the daemon with the old objectId
    daemon.register(ServerRouter, objectId=existing.object)
except Pyro5.errors.NamingError:
    print("There was no previous registration in the name server.")
    # just start a new daemon on a random port
    daemon = Daemon()
    # register the object in the daemon and let it get a new objectId
    # also need to register in name server because it's not there yet.
    uri = daemon.register(ServerRouter)
    ns.register("server.router", uri)

print("Server started.")
daemon.requestLoop()