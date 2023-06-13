from api import API

class MatchService:
    def __init__(self) -> None:
      self.__api = API()
      pass

    def getMatchById(self, params):
       response = self.__api.POST('/match-by-id', params)
       return response