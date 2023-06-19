import pyro

class MatchService:
    def __init__(self) -> None:
      self.__api = pyro.Server()
      pass

    def getMatchById(self, params):
      try:        
        response = self.__api.exec('POST', '/match-by-id', params)
        print('from server', response)
        return response
      except:
        print('Erro ao tentar buscar partida!')