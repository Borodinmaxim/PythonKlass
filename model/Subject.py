from model.base import db, Required, Optional, PrimaryKey
from model.Teacher import Teacher

class Subject(db.Entity):
    id = PrimaryKey(int, auto=True)
    item_name = Required(str)
    studying = Optional('Studying')
    teacher = Optional('Teacher')