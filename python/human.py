class Human:
    """Описание класса"""

    def __init__(self, first_name, second_name, patronymic):
        self.first_name = first_name
        self.second_name = second_name
        self.patronymic = patronymic

    """Описание методов"""

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_second_name(self, second_name):
        self.second_name = second_name

    def get_second_name(self):
        return self.second_name

    def set_patronymic(self, patronymic):
        self.patronymic = patronymic

    def get_patronymic(self):
        return self.patronymic

    """Метод: перегрузка строки, для вывода информации о классе"""

    def __str__(self):
        return f'first_name: {self.first_name}\nsecond_name: {self.second_name}\npatronymic: {self.patronymic}'
