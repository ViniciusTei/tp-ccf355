# from api import API
import pyro

class LobbyService:
  def __init__(self) -> None:
      self.__api = pyro.Server()
      pass
  
  def checkForChallengers(self, lobbyId):
      try:
        payload = {'lobbyId': lobbyId}        
        response =  self.__api.exec('POST','/check-for-challenges', payload)
        print('from server', response)
        return response
      except:
        print('Error ao buscar desafios recebidos!')

  def getAllLobbies(self, params):
      try:        
        response =  self.__api.exec('POST','/lobby-by-id', params)
        print('from server', response)
        return response
      except:
        print('Error ao buscar todas as lobbies!')

  def getLobbyPerPage(self, params):
      try:
        payload = {'page': params}        
        response =  self.__api.exec('POST','/lobby-by-page', payload)
        print('from server', response)
        return response
      except:
        print('Error ao buscar lobby por página!')

  def acceptChallenger(self, lobby_1, lobby_2):
      try:
        payload = {'requester': lobby_1, 'challenge': lobby_2}        
        response =  self.__api.exec('POST','/match', payload)
        print('from server', response)
        return response
      except:
        print('Error ao aceitar desafio entre lobbies!')