from dto.dto import DTO
from dto.klas_dto import KlasDTO
from dto.syllabus_dto import SyllabusDTO
from dto.subject_dto import SubjectDTO
from dto.teacher_dto import TeacherDTO
from dto.subtheme_dto import SubthemeDTO


class StudyingDTO(DTO):
    classes = {'klas': KlasDTO,
               'syllabus': SyllabusDTO,
               'subject': SubjectDTO,
               'teacher': TeacherDTO,
               'subtheme': SubthemeDTO}

    def __init__(self, hour: int = None, klas = None, syllabus = None, subject = None, teacher = None, sub_themes = None):
        self.hour = hour
        self.klas = klas
        self.syllabus = syllabus
        self.subject = subject
        self.teacher = teacher
        if sub_themes:
            self.sub_themes = sub_themes
        else:
            sub_themes = []

    @staticmethod
    def class_by_name(name):
        return StudyingDTO.classes[name]

    def __str__(self):
        return f'hour: {self.hour}\nklas: {self.klas}\nsyllabus: {self.syllabus} ' \
               f'\nsubject: {self.subject}\nteacher: {self.teacher}\nТемы:{", ".join([str(i) for i in self.sub_theme])} '