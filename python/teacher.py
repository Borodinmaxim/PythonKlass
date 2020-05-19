from python.human import Human


class Teacher(Human):
    """Описание класса"""
    def __init__(self, first_name, second_name, patronymic):
        super().__init__(first_name, second_name, patronymic)

    def __str__(self):
        return f'first_name: {self.first_name} second_name: {self.second_name} patronymic: {self.patronymic}'