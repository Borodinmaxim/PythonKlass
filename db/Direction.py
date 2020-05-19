from db.base import db, Required, Optional


class Direction(db.Entity):
    klas = Optional('Klas')
    name_direction = Required(str)

    def set_name_direction(self, name_direction):
        self.name_direction = name_direction

    def get_name_direction(self):
        return self.name_direction

    def __str__(self):
        return f'direction: {self.name_direction}'