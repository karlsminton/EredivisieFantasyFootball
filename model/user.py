class User:
    def __init__(self, firstname, lastname, email, password, date_of_birth, user_team_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.user_team_id = user_team_id
