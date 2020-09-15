from model.base import db, Optional,PrimaryKey
from model.Human import Human

class Teacher(Human):
    id = PrimaryKey(int, auto=True)
    subject = Optional('Subject')
    studying = Optional('Studying')
