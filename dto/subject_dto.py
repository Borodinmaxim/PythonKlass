from dto.dto import DTO
from dto.studying_dto import StudyingDTO
from dto.teacher_dto import TeacherDTO

class SubjectDTO(DTO):
    classes = {'studying': StudyingDTO,
               'teacher': TeacherDTO}

    def __init__(self, item_name = None, teacher = None):
        self.item_name = item_name
        self.teacher = teacher

    @staticmethod
    def class_by_name(name):
        return SubjectDTO.classes[name]

    def __str__(self):
        return f'item_name: {self.item_name} teacher: {self.teacher} '