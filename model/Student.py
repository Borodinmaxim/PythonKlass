from model.base import db, Required, Optional, PrimaryKey
from datetime import datetime

from model.Human import Human


class Student(Human):
    id = PrimaryKey(int, auto=True)
    result = Optional('Result')
    date = Required(datetime)