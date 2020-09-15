from dto.dto import DTO
from dto.result_dto import ResultDTO
from dto.subtheme_dto import SubthemeDTO


class TopicDTO(DTO):
    classes = {'result': ResultDTO,
               'subtheme': SubthemeDTO}

    def __init__(self, name_topic = None):
        self.name_topic = name_topic

    @staticmethod
    def class_by_name(name):
        return TopicDTO.classes[name]

    def __str__(self):
        return f'name_topic: {self.name_topic} '
