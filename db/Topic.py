from db.base import db, Required, Optional


class Topic(db.Entity):
    result = Optional('Result')
    subtheme = Optional('Subtheme')
    name_topic = Required(str)

    def set_name_topic(self, name_topic):
        self.name_topic =  self.name_topic

    def get_name_topic(self):
        return self.name_topic

    def __str__(self):
        return f'name_topic: {self.name_topic}'