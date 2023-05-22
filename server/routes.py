from router import Router as RouterClass
from controllers import sessionController, usersController, lobbyController, gamesController

Router = RouterClass()

Router.get(url='/users', callback=usersController.GetUsers)
Router.post(url='/users', callback=usersController.CreateUser)

Router.post(url='/session', callback=sessionController.PostSession)

Router.get(url='/lobby', callback=lobbyController.GetAllLobbies)
Router.post(url='/lobby', callback=lobbyController.CreateLobby)

Router.get(url='/games', callback=gamesController.GetAllGames)
