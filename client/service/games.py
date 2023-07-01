import requests

class GamesService:
  def __init__(self) -> None:
      self.__api = requests
      pass
  
  def getAllGames(self):
      try:        
        response = self.__api.get('http://127.0.0.1:5000/games')
        print('from server', response)
        return response
      except:
        print('Erro ao tentar buscar jogos!')