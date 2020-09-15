from dto.dto import DTO
from dto.klas_dto import KlasDTO

class DirectionDTO(DTO):
    classes = {'klas': KlasDTO}

    def __init__(self, name_direction = None):
        self.name_direction = name_direction

    @staticmethod
    def class_by_name(name):
        return DirectionDTO.classes[name]

    def __str__(self):
        return f'direction: {self.name_direction}'