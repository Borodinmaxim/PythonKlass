from service.service import CRUDService
from service.human_service import HumanService
from dto.student_dto import StudentDTO
from repository.student_repository import StudentRepository
from dto.result_dto import ResultDTO
from repository.result_repository import ResultRepository

class StudentService(HumanService):
    def __init__(self):
        super().__init__(StudentDTO, StudentRepository())

    def load_result(self, event):
        if event.result and event.id:
            event.order = OrderDTO.from_dict(self.order_repository.find(event.order.id))

