from pony.orm import db_session

from model.Direction import Direction
from model.Klas import Klas
from repository.repository_imp import CRUDRepositoryImp

class DirectionRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Direction)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['klas'] = Klas.get(id=args['klas']['id'])
        return args

    @staticmethod
    def to_dict(direction):
        d = direction.to_dict()
        d['klas'] = {'id': d['klas']}
        return d
