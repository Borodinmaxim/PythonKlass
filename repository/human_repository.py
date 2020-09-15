from model.Human import Human
from repository.repository_imp import CRUDRepositoryImp

class HumanRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Human)

