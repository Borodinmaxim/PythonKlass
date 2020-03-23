from python.human import Human


class Teacher(Human):
    """Описание класса"""
    def __init__(self, first_name, second_name, patronymic):
        Human.__init__(first_name, second_name, patronymic)
