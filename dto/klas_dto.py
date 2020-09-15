from dto.dto import DTO
from datetime import datetime
from dto.studying_dto import StudyingDTO
from dto.direction_dto import DirectionDTO
from dto.syllabus_dto import SyllabusDTO
from dto.student_dto import StudentDTO


class KlasDTO(DTO):
    classes = {'studying': StudyingDTO,
               'direction': DirectionDTO,
               'syllabus': SyllabusDTO,
               'student': StudentDTO}

    def __init__(self, number: int = None, date_set: datetime = None, letter=None, students = None, direction = None, syllabus = None):
        self.number = number
        self.date_set = date_set
        self.letter = letter
        self.direction = direction
        self.syllabus = syllabus
        if students:
            self.students = students
        else:
            self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    @staticmethod
    def class_by_name(name):
        return KlasDTO.classes[name]

    def __str__(self):
        return f'Дата набора: {self.date_set}\nНаправление: {self.direction} ' \
               f'\nУчебный план: {self.syllabus}\nУченики: {", ".join([str(i) for i in self.students])}'


def get_klas_dto() -> KlasDTO:
    return KlasDTO()