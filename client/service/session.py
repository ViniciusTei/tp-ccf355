import pyro

class SessionService:
  def __init__(self) -> None:
      self.__api = pyro.Server()
      pass
  
  def login(self, username, password):
      try:        
        payload = {
                "username": username,
                "password": password
            }

        response =  self.__api.exec('POST', '/session', payload)
        print('from server', response)
        return response
      except:
        print('Erro ao tentar fazer o login!')

  def createUser(self, username, password, image):
      payload = {
          'username': username,
          'password': password,
          'image': image
      }

      response =  self.__api.exec('POST', '/users', payload)
      return response
  
  def updateUser(self, username, password):
    payload = {
            "username":username,
            "password":password
        }

    response = self.__api.exec('POST', '/update', payload)
    return response