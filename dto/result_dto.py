from dto.dto import DTO
from dto.student_dto import StudentDTO
from dto.topic_dto import TopicDTO
from datetime import datetime

class ResultDTO(DTO):
    classes = {'student': StudentDTO,
               'topic': TopicDTO}

    def __init__(self, mark: int = None, datemark: datetime.date = None, student = None, topic = None):
        self.mark = mark
        self.datemark = datemark
        self.student = student
        self.topic = topic

    @staticmethod
    def class_by_name(name):
        return ResultDTO.classes[name]

    def __str__(self):
        return f'mark: {self.mark}\ndatemark: {self.datemark}\nstudent: {self.student}' \
               f'\ntopic: {self.topic} '