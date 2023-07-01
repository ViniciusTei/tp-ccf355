import requests

class ChallengesService:
  def __init__(self) -> None:
      self.__api = requests
      pass
  
  def getChallenges(self, lobbyId):
      try:      
        payload = {'lobbyid': lobbyId}  
        response = self.__api.post('http://127.0.0.1:5000/challenges', json=payload)
        print('from server', response)
        return response
      except:
        print('Erro ao tentar buscar desafios!')

  def acceptChallenge(self, challengedId, requesterId):
      try:      
        payload = { 'challengedId': challengedId, 'requesterId': requesterId }
        response = self.__api.post('http://127.0.0.1:5000/accept-challenge', json=payload)
        print('from server', response)
        return response
      except:
        print('Erro ao tentar aceitar desafio!')
  
  def rejectChallenge(self, challengedId, requesterId):
      try:      
        payload = { 'challengedId': challengedId, 'requesterId': requesterId }
        response = self.__api.post('http://127.0.0.1:5000/reject-challenge', json=payload)
        print('from server', response)
        return response
      except:
        print('Erro ao tentar rejeitar desafio!')