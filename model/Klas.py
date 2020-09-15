from model.base import db, Required, Optional, PrimaryKey
from datetime import datetime
from model.Direction import Direction
from model.Syllabus import Syllabus

class Klas(db.Entity):
    id = PrimaryKey(int, auto=True)
    studying = Optional('Studying')
    number = Optional(int)
    date_set = Required(datetime)
    letter = Required(str)
    direction = Required('Direction')
    syllabus = Required('Syllabus')
    students = []