from db.base import db, Required, Optional
from datetime import datetime
from db.Direction import Direction
from db.Syllabus import Syllabus

class Klas(db.Entity):
    studying = Optional('Studying')
    number = Optional(int)
    date_set = Required(datetime)
    letter = Required(str)
    direction = Required(Direction)
    syllabus = Required(Syllabus)
    students = []

    def add_student(self, student):
        self.students.append(student)

    def del_student(self, student):
        self.students.remove(student)

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def set_date_set(self, date_set):
        self.date_set = date_set

    def get_date_set(self):
        return self.date_set

    def set_letter(self, letter):
        self.letter = letter

    def get_letter(self):
        return self.letter

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_syllabus(self, syllabus):
        self.syllabus = syllabus

    def get_syllabus(self):
        return self.syllabus

    def get_number_today(self):
        d = datetime(2012, 9, 11)
        t = datetime.now()
        number = t - d
        return number.days // 365 + 1

    def __str__(self):
        return f'Дата набора: {self.date_set}\nНаправление: {self.direction} ' \
               f'\nУчебный план: {self.syllabus}\nУченики: {", ".join([str(i) for i in self.students])}'