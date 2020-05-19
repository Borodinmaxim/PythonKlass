from db.base import db, Required, Optional
from db.Student import Student
from db.Topic import Topic
import datetime


class Result(db.Entity):
    student = Optional('Student')
    mark = Required(int)
    datemark = Optional(datetime.datetime)
    topic = Optional('Topic')

    def set_mark(self, mark):
        self.mark = mark

    def get_mark(self):
        return self.mark

    def set_datemark(self, datemark):
        self.datemark = datemark

    def get_datemark(self):
        return self.datemark

    def set_student(self, student):
        self.student = student

    def get_student(self):
        return self.student

    def set_topic(self, topic):
        self.topic = self.topic

    def get_topic(self):
        return self.topic

    def __str__(self):
        return f'mark: {self.mark}\ndatemark: {self.datemark}\nstudent: {self.student}' \
               f'\ntopic: {self.topic}'
