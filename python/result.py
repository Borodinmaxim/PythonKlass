from python.student import Student
from python.topic import Topic
import datetime


class Result:
    def __init__(self, mark: int, datemark: datetime.date, student: Student, topic: Topic):
        self.mark = mark
        self.datemark = datemark
        self.student = student
        self.topic = topic

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
        self.topic =  self.topic

    def get_topic(self):
        return self.topic

    def __str__(self):
        return f'mark: {self.mark}\ndatemark: {self.datemark}\nstudent: {self.student}' \
               f'\ntopic: {self.topic} '