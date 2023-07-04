import requests

class Steam:
    def __init__(self) -> None:
        self.__baseUrl = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'
        pass
    
    # Busca na api da steam todos os jogos da plataforma
    # o resultado eh no formato:
    # applist: {
    # { apps: [
    #    { appid: number, name: string }
    # ] }
    def getAllGamesFromSteam(self):
        response = requests.get(self.__baseUrl)
        responseJson = response.json()
        data = responseJson['applist']['apps']
        return data