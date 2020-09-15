from model.base import db, Required, Optional, PrimaryKey


class Syllabus(db.Entity):
    id = PrimaryKey(int, auto=True)
    studying = Optional('Studying')
    klas = Optional('Klas')
    start = Required(str)
    finish = Required(str)