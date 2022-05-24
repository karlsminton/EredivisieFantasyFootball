import json
from http import client
from model.player import Player
from model.repository import Repository

# Credentials
api_key = 'd721aa936e2644de9391789cf0b2c441'
url = 'api.football-data.org'
headers = {'X-Auth-Token': api_key}
params = None

# Get data from URL
connection = client.HTTPConnection(url, '80')
connection.request('GET', '/v2/teams/678', params, headers)
response = connection.getresponse()
string = response.read().decode('utf-8', 'ignore')

# Transform data to JSON
decoder = json.JSONDecoder()
api_response = decoder.decode(string)

items = api_response['squad']

for item in items:
    plyr = Player(
        item['name'],
        item['position'],
        item['dateOfBirth'],
        item['nationality'],
        item['shirtNumber']
    )

    Repository().save(plyr)
