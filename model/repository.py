from mariadb import connect
import datetime
import re


class Repository:
    TABLE = 'players'

    def __init__(self):
        self.connection = connect(
            user="eredivisie",
            password="eredivisie",
            host="localhost",
            database="eredivisie"
        )
        self.cursor = self.connection.cursor()

    def save(self, player):
        query = """
        INSERT INTO players 
        (name, position, date_of_birth, nationality, shirt_number)
        VALUES (?, ?, ?, ?, ?)
        """

        # TODO get enum 'positions' working
        positions = {'GOALKEEPER': 0, 'DEFENCE': 1, 'MIDFIELD': 2, 'OFFENCE': 3}
        player_position = positions[player.position.upper()]

        search = re.search('\d{4}\-\d{2}\-\d{2}', player.date_of_birth)
        date = search.group(0)

        dob = datetime.datetime.fromisoformat(date)

        values = (
            player.name,
            player_position,
            dob,
            player.nationality,
            player.shirt_number or 1
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
