import json
from http import client


class Request:
    def __init__(self):
        api_key = 'd721aa936e2644de9391789cf0b2c441'
        url = 'api.football-data.org'
        self.headers = {'X-Auth-Token': api_key}
        self.params = None
        self.connection = client.HTTPConnection(url, '80')
        self.decoder = json.JSONDecoder()

    def get_from_endpoint(self, endpoint, method="GET"):
        self.connection.request(method, endpoint, self.params, self.headers)
        response = self.connection.getresponse()
        string = response.read().decode('utf-8', 'ignore')
        api_response = self.decoder.decode(string)
        return api_response
