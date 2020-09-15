from pony.orm import db_session

from model.Syllabus import Syllabus
from model.Studying import Studying
from model.Klas import Klas
from repository.repository_imp import CRUDRepositoryImp

class SyllabusRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Syllabus)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['studying'] = Studying.get(id=args['studying']['id'])
        args['klas'] = Klas.get(id=args['klas']['id'])
        return args

    @staticmethod
    def to_dict(syllabus):
        d = syllabus.to_dict()
        d['studying'] = {'id': d['studying']}
        d['klas'] = {'id': d['klas']}
        return d