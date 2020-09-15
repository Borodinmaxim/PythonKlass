from model.base import db, Required, Optional, PrimaryKey
from model.Studying import Studying
from model.Topic import Topic

class Subtheme(db.Entity):
    id = PrimaryKey(int, auto=True)
    studying = Optional('Studying')
    topic = Optional('Topic')

