import requests
import os

def uploadImage(payload):
    filePath = os.getcwd() + '/server/temp/' + payload['file_name']
    formData = {
        'key': '6d207e02198a847aa98d0a2a901485a5',
        'source': open(filePath)
    }
    response = requests.post(url="https://freeimage.host/api/1/upload", data=formData)
    try:
      data = response.json()     
      print(data)                
    except requests.exceptions.RequestException:
      print(response.text)