from model.base import db, Required, Optional, PrimaryKey
from model.Student import Student
from model.Topic import Topic
import datetime


class Result(db.Entity):
    id = PrimaryKey(int, auto=True)
    student = Optional('Student')
    mark = Required(int)
    datemark = Optional(datetime.datetime)
    topic = Optional('Topic')
