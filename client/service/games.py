from .steam import Steam

class GamesService:
  def __init__(self) -> None:
      self.__api = Steam()
      pass
  
  def getAllGames(self):
      try:        
        response = self.__api.getAllGamesFromSteam()
        print('from steam', response)
        return response
      except:
        print('Erro ao tentar buscar jogos!')