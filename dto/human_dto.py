from dto.dto import DTO

class HumanDTO(DTO):
    def __init__(self, id=None, first_name=None, second_name=None, patronymic=None):
        self.first_name = first_name
        self.second_name = second_name
        self.patronymic = patronymic
        self.id = id

    def __str__(self):
        return f'first_name: {self.first_name}\nsecond_name: {self.second_name}\npatronymic: {self.patronymic}'
