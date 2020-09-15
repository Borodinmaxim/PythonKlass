from dto.dto import DTO
from dto.human_dto import HumanDTO
from dto.result_dto import ResultDTO
from datetime import datetime

class StudentDTO(HumanDTO):
    classes = {'result': ResultDTO}

    def __init__(self, date: datetime = None, first_name = None, second_name = None, patronymic = None):
        super().__init__(first_name, second_name, patronymic)
        self.date = date

    @staticmethod
    def class_by_name(name):
        return StudentDTO.classes[name]

    def __str__(self):
        return f'Фамилия: {self.first_name} Имя: {self.second_name} Отчество: {self.patronymic} ' \
               f'Дата рождения: {self.date}'
