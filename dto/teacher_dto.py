from dto.dto import DTO
from dto.human_dto import HumanDTO
from dto.subject_dto import SubjectDTO
from dto.studying_dto import StudyingDTO

class TeacherDTO(HumanDTO):
    classes = {'subject': SubjectDTO,
               'studying': StudyingDTO}

    def __init__(self, first_name = None, second_name = None, patronymic = None):
        super().__init__(first_name, second_name, patronymic)

    @staticmethod
    def class_by_name(name):
        return TeacherDTO.classes[name]

    def __str__(self):
        return f'first_name: {self.first_name} second_name: {self.second_name} patronymic: {self.patronymic}'