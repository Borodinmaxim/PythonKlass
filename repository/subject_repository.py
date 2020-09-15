from pony.orm import db_session

from model.Subject import Subject
from model.Studying import Studying
from model.Teacher import Teacher
from repository.repository_imp import CRUDRepositoryImp

class SubjectRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Subject)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['studying'] = Studying.get(id=args['studying']['id'])
        args['teacher'] = Teacher.get(id=args['teacher']['id'])
        return args

    @staticmethod
    def to_dict(subject):
        d = subject.to_dict()
        d['studying'] = {'id': d['studying']}
        d['teacher'] = {'id': d['teacher']}
        return d