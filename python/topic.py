class Topic:
    """Описание класса"""

    def __init__(self, name_topic):
        self.name_topic = name_topic
        """Описание методов"""

    def set_name_topic(self, name_topic):
        self.name_topic =  self.name_topic

    def get_name_topic(self):
        return self.name_topic

    def __str__(self):
        return f'name_topic: {self.name_topic} '

