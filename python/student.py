from datetime import datetime

from python.human import Human


class Student(Human):
    def __init__(self, date: datetime, first_name, second_name, patronymic):
        super().__init__(first_name, second_name, patronymic)
        self.date = date

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def __str__(self):
        return f'Фамилия: {self.first_name} Имя: {self.second_name} Отчество: {self.patronymic} ' \
               f'Дата рождения: {self.date}'
