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
        query = 'SELECT * FROM %s WHERE user_id = %s'
        values = (self.TABLE, user_id)
        self.cursor.execute(query, values)
        results = self.cursor.fetchone()
        # return User()

    def delete_by_id(self, user_id):
        query = 'DELETE FROM %s WHERE user_id = %s'
        values = (self.TABLE, user_id)
        self.cursor.execute(query, values)
        self.connection.commit()
