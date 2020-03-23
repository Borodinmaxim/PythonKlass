class Topic:
    """Описание класса"""

    def __init__(self, name_topic):
        self.name_topic = name_topic
        self.topics = []
        """Описание методов"""

    def add_topic(self, topic):
        self.topics.append(topic)

    def del_topic(self, topic):
        self.topics.remove(topic)

    def set_name_topic(self, name_topic):
        self.name_topic

    def get_name_topic(self):
        return self.name_topic
