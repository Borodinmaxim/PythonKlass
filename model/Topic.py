from model.base import db, Required, Optional,PrimaryKey


class Topic(db.Entity):
    id = PrimaryKey(int, auto=True)
    result = Optional('Result')
    subtheme = Optional('Subtheme')
    name_topic = Required(str)