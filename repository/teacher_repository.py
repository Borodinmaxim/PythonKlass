from pony.orm import db_session

from model.Teacher import Teacher
from model.Subject import Subject
from model.Studying import Studying
from repository.repository_imp import CRUDRepositoryImp

class TeacherRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Teacher)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['subject'] = Subject.get(id=args['subject']['id'])
        args['studying'] = Studying.get(id=args['studying']['id'])
        return args

    @staticmethod
    def to_dict(teacher):
        d = teacher.to_dict()
        d['subject'] = {'id': d['subject']}
        d['studying'] = {'id': d['studying']}
        del d['classtype']
        return d