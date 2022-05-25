from cron.request import Request
from model.club import Club
from model.club_repository import ClubRepository

# Credentials
request = Request()

# Get data from URL
api_response = request.get_from_endpoint('/v2/competitions/2003/standings')
standings = api_response['standings']
items = standings[0]['table']

for item in items:
    clb = Club(
        item['team']['id'],
        item['team']['name'],
        item['team']['name'],
        item['team']['crestUrl']
    )
    ClubRepository().save(clb)
