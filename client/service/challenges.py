import pyro

class ChallengesService:
  def __init__(self) -> None:
      self.__api = pyro.Server()
      pass
  
  def getChallenges(self, lobbyId):
      try:      
        payload = {'lobbyid': lobbyId}  
        response =  self.__api.exec('POST', '/challenges', payload)
        print('from server', response)
        return response
      except:
        print('Erro ao tentar buscar desafios!')

  def acceptChallenge(self, challengedId, requesterId):
      try:      
        payload = { 'challengedId': challengedId, 'requesterId': requesterId }
        response =  self.__api.exec('POST', '/accept-challenge', payload)
        print('from server', response)
        return response
      except:
        print('Erro ao tentar aceitar desafio!')
  
  def rejectChallenge(self, challengedId, requesterId):
      try:      
        payload = { 'challengedId': challengedId, 'requesterId': requesterId }
        response =  self.__api.exec('POST', '/reject-challenge', payload)
        print('from server', response)
        return response
      except:
        print('Erro ao tentar rejeitar desafio!')