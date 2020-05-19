from db.base import db, Required, Optional
from db.Teacher import Teacher

class Subject(db.Entity):
    item_name = Required(str)
    studying = Optional('Studying')
    teacher = Optional('Teacher')

    def set_item_name(self, item_name):
        self.item_name = item_name

    def get_item_name(self):
        return self.item_name

    def set_teacher(self, teacher):
        self.teacher = teacher

    def get_teacher(self):
        return self.teacher


    def __str__(self):
        return f'item_name: {self.item_name} teacher: {self.teacher}'