from python.syllabus import Syllabus
from python.direction import Direction
from datetime import datetime


class Klas:
    def __init__(self, number: int = None, date_set: datetime = None, letter = None, direction: Direction = None, syllabus: Syllabus = None,):
        self.number = number
        self.date_set = date_set
        self.letter = letter
        self.direction = direction
        self.syllabus = syllabus
        self.students = []


    def __str__(self):
        return f'Дата набора: {self.date_set}\nНаправление: {self.direction} ' \
               f'\nУчебный план: {self.syllabus}\nУченики: {", ".join([str(i) for i in self.students])}'

    def prt_students(self):
        for x in self.students:
            if x != None:
                print(x)


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
