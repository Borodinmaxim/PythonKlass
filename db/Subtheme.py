from db.base import db, Required, Optional
from db.Studying import Studying
from db.Topic import Topic

class Subtheme(db.Entity):
    studying = Optional('Studying')
    topic = Optional('Topic')

    def set_studying(self, studying):
        self.studying = studying

    def get_studying(self):
        return self.studying

    def set_topic(self, topic):
        self.topic = topic

    def get_topic(self):
        return self.topic

    def __str__(self):
        return f'topic: {self.topic}'