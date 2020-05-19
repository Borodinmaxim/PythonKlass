from db.base import db, Optional
from db.Human import Human

class Teacher(Human):
    subject = Optional('Subject')
    studying = Optional('Studying')


    def __str__(self):
        return f'first_name: {self.first_name} second_name: {self.second_name} patronymic: {self.patronymic}'