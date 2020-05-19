class Direction:
    """Описание класса"""

    def __init__(self, name_direction):
        self.name_direction = name_direction

    """Описание методов"""

    def set_name_direction(self, name_direction):
        self.name_direction = name_direction

    def get_name_direction(self):
        return self.name_direction

    def __str__(self):
        return f'direction: {self.name_direction}'

