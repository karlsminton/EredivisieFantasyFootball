from mariadb import connect
import datetime
import re
from model.user import User


class UserRepository:
    TABLE = 'users'

    def __init__(self):
        self.connection = connect(
            user="eredivisie",
            password="eredivisie",
            host="localhost",
            database="eredivisie"
        )
        self.cursor = self.connection.cursor()

    def save(self, user):
        query = """
        INSERT INTO users 
        (firstname, lastname, email, password, date_of_birth, user_team_id)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        # dob = datetime.datetime.fromisoformat(date)

        values = (
            user.firstname,
            user.lastname,
            user.email,
            user.password,
            user.date_of_birth,
            user.user_team_id
        )

        self.cursor.execute(query, values)
        self.connection.commit()

    def load_by_id(self, user_id):
        query = 'SELECT * FROM ' + self.TABLE + ' WHERE user_id = %s'
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def delete_by_id(self, user_id):
        query = 'DELETE FROM ' + self.TABLE + ' WHERE user_id = %s'
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
