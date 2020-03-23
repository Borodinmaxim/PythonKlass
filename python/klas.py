from python.syllabus import Syllabus
from python.direction import Direction
import datetime


class Klas:
    def __init__(self, date: datetime.date, letter, direction: Direction, syllabus: Syllabus, now):
        self.date = datetime.date(2013, 3, 20)
        self.letter = letter
        self.direction = direction
        self.syllabus = syllabus
        self.students = []
        self.now = datetime.date.today()

    def add_student(self, student):
        self.students.append(student)

    def del_student(self, student):
        self.students.remove(student)

    """def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date"""

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
