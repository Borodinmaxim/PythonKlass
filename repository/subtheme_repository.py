from pony.orm import db_session

from model.Subtheme import Subtheme
from model.Studying import Studying
from model.Topic import Topic
from repository.repository_imp import CRUDRepositoryImp

class SubthemeRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Subtheme)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['studying'] = Studying.get(id=args['studying']['id'])
        args['topic'] = Topic.get(id=args['topic']['id'])
        return args

    @staticmethod
    def to_dict(subtheme):
        d = subtheme.to_dict()
        d['studying'] = {'id': d['studying']}
        d['topic'] = {'id': d['topic']}
        return d