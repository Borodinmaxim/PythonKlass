from python.teacher import Teacher


class Subject:
    """Описание класса"""

    def __init__(self, item_name, teacher: Teacher):
        self.item_name = item_name
        self.teacher = teacher

    """Описание методов"""

    def set_item_name(self, item_name):
        self.item_name

    def get_item_name(self):
        return self.item_name

    def set_teacher(self, teacher):
        self.teacher

    def get_teacher(self):
        return self.teacher


    def __str__(self):
        return f'item_name: {self.item_name} teacher: {self.teacher} '