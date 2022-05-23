import datetime as dt

from marshmallow import Schema, fields


class Player:
    def __init__(self, name, position, date_of_birth, nationality, shirt_number):
        self.name = name
        self.position = position
        self.date_of_birth = date_of_birth
        self.nationality = nationality
        self.shirt_number = shirt_number

    def __repr__(self):
        return '<Player(name={self.name!r})>'.format(self=self)


class PlayerSchema(Schema):
    name = fields.Str()
    position = fields.Str()
    date_of_birth = fields.Date()
    nationality = fields.Str()
    shirt_number = fields.Number()
