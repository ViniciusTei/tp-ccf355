from router import Router as RouterClass
from controllers import sessionController, usersController, lobbyController, gamesController, matchController

Router = RouterClass()

Router.get(url='/users', callback=usersController.GetUsers)
Router.post(url='/users', callback=usersController.CreateUser)

Router.post(url='/session', callback=sessionController.PostSession)

# depecrated, use lobby-by-page instead
Router.get(url='/lobby', callback=lobbyController.GetAllLobbies)
Router.post(url='/lobby', callback=lobbyController.CreateLobby)
Router.post(url='/lobby-by-id', callback=lobbyController.GetLobbyById)
Router.post(url='/lobby-enter', callback=lobbyController.EnterLobby)
Router.post(url='/lobby-leave', callback=lobbyController.LeaveLobby)
Router.post(url='/lobby-by-page', callback=lobbyController.GetAllLobbies)

Router.get(url='/games', callback=gamesController.GetAllGames)

Router.post(url='/match', callback=matchController.Create)
Router.post(url='/match-by-id', callback=matchController.GetMatch)

Router.post(url='/challenges', callback=matchController.GetAllChallenges)
Router.post(url='/accept-challenge', callback=matchController.AcceptChallenge)
Router.post(url='/reject-challente', callback=matchController.RejectChallenge)
Router.post(url='/check-for-challenges', callback=matchController.CheckForLobbies)
