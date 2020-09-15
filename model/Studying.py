from model.base import db, Required, Optional, PrimaryKey


class Studying(db.Entity):
    id = PrimaryKey(int, auto=True)
    hour = Optional(int)
    klas = Optional('Klas')
    syllabus = Optional('Syllabus')
    subject = Optional('Subject')
    teacher = Optional('Teacher')
    subtheme = Optional('Subtheme')
    sub_theme = []