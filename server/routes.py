from router import Router as RouterClass
from controllers import sessionController, usersController, lobbyController

Router = RouterClass()

Router.get(url='/users', callback=usersController.GetUsers)
Router.post(url='/users', callback=usersController.CreateUser)

Router.post(url='/session', callback=sessionController.PostSession)

Router.post(url='/lobby', callback=lobbyController.GetAllLobbies)
