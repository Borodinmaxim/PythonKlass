from datetime import date

from python.human import Human


class Student(Human):
    def __init__(self, date: date, first_name, second_name, patronymic):
        Human.__init__(first_name, second_name, patronymic)
        self.date = date

    def set_klass(self, date):
        self.date = date

    def get_klass(self):
        return self.date

    def __str__(self):
        return f'first_name:\n{self.first_name}\nsecond_name:\n{self.second_name}\npatronymic:\n{self.patronymic}\n' \
               f'date:\n{self.date}'
