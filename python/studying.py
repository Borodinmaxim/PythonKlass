from python.klas import Klas
from python.syllabus import Syllabus
from python.subject import Subject
from python.teacher import Teacher


class Studying:
    def __init__(self, hour: int, klas: Klas, syllabus: Syllabus, subject: Subject, teacher: Teacher):
        self.hour = hour
        self.klas = klas
        self.syllabus = syllabus
        self.subject = subject
        self.teacher = teacher

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
        self.subject

    def get_subject(self):
        return self.subject

    def set_teacher(self, teacher):
        self.teacher = teacher

    def get_teacher(self):
        return self.teacher