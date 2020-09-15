from pony.orm import db_session

from model.Student import Student
from repository.repository_imp import CRUDRepositoryImp

class StudentRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Student)

    @staticmethod
    @db_session
    def from_dict(student):
        args = student
        args['result'] = Student.get(id=args['result']['id'])
        return args

    @staticmethod
    def to_dict(student):
        d = student.to_dict()
        d['result'] = {'id': d['result']}
        del d['classtype']
        return d