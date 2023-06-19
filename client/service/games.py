import pyro

class GamesService:
  def __init__(self) -> None:
      self.__api = pyro.Server()
      pass
  
  def getAllGames(self):
      try:        
        response =  self.__api.exec('GET', '/games')
        print('from server', response)
        return response
      except:
        print('Erro ao tentar buscar jogos!')