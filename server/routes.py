from router import Router as RouterClass
from controllers import sessionController, usersController

Router = RouterClass()

Router.get(url='/users', callback=usersController.GetUsers)
Router.post(url='/session', callback=sessionController.PostSession)
# Router.post(url='/upload', callback=uploadController.upload)
