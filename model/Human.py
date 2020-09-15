from model.base import db, Required, PrimaryKey


class Human(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    second_name = Required(str)
    patronymic = Required(str)