from api import API

class SessionService:
  def __init__(self) -> None:
      self.__api = API()
      pass
  
  def login(self, username, password):
      try:        
        payload = {
                "username": username,
                "password": password
            }

        response =  self.__api.POST('/session', payload)
        return response
      except:
        print('Erro ao tentar fazer o login!')

  def createUser(self, username, password, image):
      payload = {
          'username': username,
          'password': password,
          'image': image
      }

      response =  self.__api.POST('/users', payload)
      return response
  
  def updateUser(self, username, password):
    payload = {
            "username":username,
            "password":password
        }

    response = self.__api.POST('/update', payload)
    return response