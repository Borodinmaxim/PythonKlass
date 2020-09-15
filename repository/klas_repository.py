from pony.orm import db_session

from model.Klas import Klas
from model.Studying import Studying

from repository.repository_imp import CRUDRepositoryImp

class KlasRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Klas)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['studying'] = Studying.get(id=args['studying']['id'])
        return args

    @staticmethod
    def to_dict(klas):
        d = klas.to_dict()
        d['studying'] = {'id': d['studying']}
        return d