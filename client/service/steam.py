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
        
        try:

            response = requests.get(self.__baseUrl)
            responseJson = response.json()
            data = responseJson.get('appList', {}).get('apps', {})

            return data
        except requests.exceptions.RequestsException as e:
            print('Erro de requisicao', e)
        except json.JSONDecodeError as e:
            print('Erro de dados', e)

        return []
