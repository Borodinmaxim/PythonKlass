from pony.orm import db_session

from model.Topic import Topic
from model.Result import Result
from model.Subtheme import Subtheme
from repository.repository_imp import CRUDRepositoryImp

class TopicRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Topic)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['result'] = Result.get(id=args['result']['id'])
        args['subtheme'] = Subtheme.get(id=args['subtheme']['id'])
        return args

    @staticmethod
    def to_dict(topic):
        d = topic.to_dict()
        d['result'] = {'id': d['result']}
        d['subtheme'] = {'id': d['subtheme']}
        return d