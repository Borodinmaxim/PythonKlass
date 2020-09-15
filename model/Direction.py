from model.base import db, Required, Optional, PrimaryKey


class Direction(db.Entity):
    id = PrimaryKey(int, auto=True)
    klas = Optional('Klas')
    name_direction = Required(str)