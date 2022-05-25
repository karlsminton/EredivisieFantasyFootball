from mariadb import connect


class ClubRepository:
    TABLE = 'clubs'

    def __init__(self):
        self.connection = connect(
            user="eredivisie",
            password="eredivisie",
            host="localhost",
            database="eredivisie"
        )
        self.cursor = self.connection.cursor()

    def save(self, club):
        query = """
        INSERT INTO clubs 
        (api_id, name, short_name, crest_url, website, venue)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        values = (
            club.api_id,
            club.name,
            club.short_name,
            club.crest_url,
            club.website,
            club.venue
        )

        self.cursor.execute(query, values)
        self.connection.commit()

    def load_by_id(self, club_id):
        query = 'SELECT * FROM ? WHERE id = ?'
        values = (self.TABLE, club_id)
        self.cursor.execute(query, values)
        results = self.cursor.fetchone()
        # loaded = Player.Player()

    def delete_by_id(self, club_id):
        query = 'DELETE FROM %s WHERE club_id = %s'
        values = (self.TABLE, club_id)
        self.cursor.execute(query, values)
        self.connection.commit()
