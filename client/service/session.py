import requests

class SessionService:
  def __init__(self) -> None:
      self.__api = requests
      pass
  
  def login(self, username, password):
      try:        
        payload = {
                "username": username,
                "password": password
            }

        response = self.__api.post('http://127.0.0.1:5000/session', json=payload)
        return response.json()
      except:
        print('Erro ao tentar fazer o login!')

  def createUser(self, username, password, image):
      payload = {
          'username': username,
          'password': password,
          'image': image
      }

      response =  self.__api.post('http://127.0.0.1:5000/users', json=payload)
      return response
  
  def updateUser(self, username, password):
    payload = {
            "username":username,
            "password":password
        }

    response = self.__api.post('http://127.0.0.1:5000/update', json=payload)
    return response