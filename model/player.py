class Player:
    def __init__(self, name, position, date_of_birth, nationality, shirt_number):
        self.name = name
        self.position = position
        self.date_of_birth = date_of_birth
        self.nationality = nationality
        self.shirt_number = shirt_number

    def __repr__(self):
        return '<Player(name={self.name!r})>'.format(self=self)
