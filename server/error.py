import json

class Error:
  def __init__(self, message, status):
    self.__msg = message
    self.__status = status
    pass
  
  def toDict(self):
    return {
      'message': self.__msg,
      'status': self.__status
    }
  
  def toString(self):
    return json.dumps(self.toDict())