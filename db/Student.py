from db.base import db, Required, Optional
from datetime import datetime

from db.Human import Human


class Student(Human):
    result = Optional('Result')
    date = Required(datetime)


    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def __str__(self):
        return f'Фамилия: {self.first_name} Имя: {self.second_name} Отчество: {self.patronymic} ' \
               f'Дата рождения: {self.date}'
