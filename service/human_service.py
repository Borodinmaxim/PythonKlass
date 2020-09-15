from service.service import CRUDService
from dto.human_dto import HumanDTO
from repository.human_repository import HumanRepository

class HumanService(CRUDService):
    def __init__(self):
        super().__init__(HumanDTO,HumanRepository())