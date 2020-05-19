class Syllabus:
    """Описание класса"""

    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    """Описание методов"""

    def set_start(self, start):
        self.start = start

    def get_start(self):
        return self.start

    def set_finish(self, finish):
        self.finish = finish

    def get_finish(self):
        return self.finish

    def __str__(self):
        return f'Начало: {self.start} Конец: {self.finish}'
