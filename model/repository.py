from mysql import connector
import player as Player


class Repository:
    TABLE = 'players'

    def __init__(self):
        self.connection = connector.connect(
            user="eredivisie",
            password="eredivisie",
            host="localhost",
            database="eredivisie"
        )
        self.cursor = self.connection.cursor()

    def save(self, player):
        query = """
        INSERT INTO %s 
        (name, position, date_of_birth, nationality, shirt_number)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            self.TABLE,
            player.name,
            player.position,
            player.date_of_birth,
            player.nationality,
            player.shirt_number
        )

        self.cursor.execute(query, values)
        self.connection.commit()

    def load_by_id(self, player_id):
        query = 'SELECT * FROM %s WHERE id = %s'
        values = (self.TABLE, player_id)
        self.cursor.execute(query, values)
        results = self.cursor.fetchone()
        # loaded = Player.Player()

    def delete_by_id(self, player_id):
        query = 'DELETE FROM %s WHERE id = %s'
        values = (self.TABLE, player_id)
        self.cursor.execute(query, values)
        self.connection.commit()
