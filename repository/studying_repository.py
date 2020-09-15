from pony.orm import db_session

from model.Studying import Studying
from model.Klas import Klas
from model.Syllabus import Syllabus
from model.Subject import Subject
from model.Teacher import Teacher
from model.Subtheme import Subtheme
from repository.repository_imp import CRUDRepositoryImp

class StudyingRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Studying)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['klas'] = Klas.get(id=args['klas']['id'])
        args['syllabus'] = Syllabus.get(id=args['syllabus']['id'])
        args['subject'] = Subject.get(id=args['subject']['id'])
        args['teacher'] = Teacher.get(id=args['teacher']['id'])
        args['subtheme'] = Subtheme.get(id=args['subtheme']['id'])
        return args

    @staticmethod
    def to_dict(studying):
        d = studying.to_dict()
        d['klas'] = {'id': d['klas']}
        d['syllabus'] = {'id': d['syllabus']}
        d['subject'] = {'id': d['subject']}
        d['teacher'] = {'id': d['teacher']}
        d['subtheme'] = {'id': d['subtheme']}
        return d