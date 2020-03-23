from python.student import Student
import datetime


class Result:
    def __init__(self, mark: int, datemark: datetime.date, student: Student):
        self.mark = mark
        self.datemark = datemark
        self.student = student

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
