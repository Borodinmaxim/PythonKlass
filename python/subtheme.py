from python.studying import Studying
from python.topic import Topic


class Subtheme:
    def __init__(self, studying: Studying, topic: Topic):
        self.studying = studying
        self.topic = topic

    def set_studying(self, studying):
        self.studying = studying

    def get_studying(self):
        return self.studying

    def set_topic(self, topic):
        self.topic = topic

    def get_topic(self):
        return self.topic
