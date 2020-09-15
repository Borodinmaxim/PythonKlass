from dto.dto import DTO
from dto.studying_dto import StudyingDTO
from dto.klas_dto import KlasDTO


class SyllabusDTO(DTO):
    classes = {'studying': StudyingDTO,
               'klas': KlasDTO}

    def __init__(self, start= None, finish = None):
        self.start = start
        self.finish = finish

    @staticmethod
    def class_by_name(name):
        return SyllabusDTO.classes[name]

    def __str__(self):
        return f'Начало: {self.start} Конец: {self.finish}'