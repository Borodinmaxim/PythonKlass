from db.base import db, Required, Optional
from db.Klas import Klas
from db.Syllabus import Syllabus
from db.Subject import Subject
from db.Teacher import Teacher

class Studying(db.Entity):
    hour = Optional(int)
    klas = Optional('Klas')
    syllabus = Optional('Syllabus')
    subject = Optional('Subject')
    teacher = Optional('Teacher')
    subtheme = Optional('Subtheme')
    sub_theme = []

    def get_sub_themes(self):
        return self.sub_theme

    def set_house(self, hour):
        self.hour = hour

    def get_hour(self):
        return self.hour

    def set_klas(self, klas):
        self.klas = klas

    def get_klas(self):
        return self.klas

    def set_syllabus(self, syllabus):
        self.syllabus = syllabus

    def get_syllabus(self):
        return self.syllabus

    def set_subject(self, subject):
        self.subject = subject

    def get_subject(self):
        return self.subject

    def set_teacher(self, teacher):
        self.teacher = teacher

    def get_teacher(self):
        return self.teacher

    def __str__(self):
        return f'hour: {self.hour}\nklas: {self.klas}\nsyllabus: {self.syllabus} ' \
               f'\nsubject: {self.subject}\nteacher: {self.teacher}\nТемы:{", ".join([str(i) for i in self.sub_theme])}'