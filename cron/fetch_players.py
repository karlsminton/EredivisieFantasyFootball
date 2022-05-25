from cron.request import Request
from model.player import Player
from model.player_repository import PlayerRepository

# Credentials
request = Request()

# Get data from URL
api_response = request.get_from_endpoint('/v2/teams/678')
items = api_response['squad']

for item in items:
    plyr = Player(
        item['name'],
        item['position'],
        item['dateOfBirth'],
        item['nationality'],
        item['shirtNumber']
    )

    PlayerRepository().save(plyr)
