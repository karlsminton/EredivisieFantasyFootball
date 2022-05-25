class Club:
    def __init__(self, api_id, name, short_name, crest_url, website=None, venue=None):
        self.api_id = api_id
        self.name = name
        self.short_name = short_name
        self.crest_url = crest_url
        self.website = website
        self.venue = venue

    def __repr__(self):
        return '<Club(name={self.name!r})>'.format(self=self)
