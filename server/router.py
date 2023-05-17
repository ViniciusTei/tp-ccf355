from error import Error

STATUS = {
    'SUCCESS': 200,
    'NOTFOUND': 400,
    'ERROR': 500
}

class Router:
    def __init__(self) -> None:
        self.__get = []
        self.__post = []
        pass
    
    def get(self, url, callback):
        self.__get.append({
            "url": url,
            "callback": callback
        })
    
    def post(self, url, callback):
        self.__post.append({
            "url": url,
            "callback": callback
        })

    def run(self, method, url, payload):
        if method == 'GET':
            for route in self.__get:
                if route['url'] == url:
                    print('GET',  route['url'])
                    return route['callback']()
            
            return Error('Route not found', STATUS['NOTFOUND']).toString()

        elif method == 'POST':
            for route in self.__post:
                if route['url'] == url:
                    print('POST', route['url'], payload)
                    return route['callback'](payload)
                
            return Error('Route not found', STATUS['NOTFOUND']).toString()

        else:
            print('Method not allowed')
            return Error('Method not allowed', STATUS['ERROR']).toString()