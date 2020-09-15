from dto.dto import DTO
from dto.studying_dto import StudyingDTO
from dto.topic_dto import TopicDTO


class SubthemeDTO(DTO):
    classes = {'studying': StudyingDTO,
               'topic': TopicDTO}

    def __init__(self, studying = None, topic = None):
        self.studying = studying
        self.topic = topic

    @staticmethod
    def class_by_name(name):
        return SubthemeDTO.classes[name]

    def __str__(self):
        return f'topic: {self.topic} '