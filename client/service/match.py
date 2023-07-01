import requests

class MatchService:
    def __init__(self) -> None:
      self.__api = requests
      pass

    def getMatchById(self, params):
      try:
        response = self.__api.post('http://127.0.0.1:5000/match-by-id', json=params)        
        print('from server', response)
        return response
      except:
        print('Erro ao tentar buscar partida!')