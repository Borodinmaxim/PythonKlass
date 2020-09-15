from model.base import db, db_session
from datetime import *
from model.Direction import Direction
from model.Klas import Klas
from model.Result import Result
from model.Student import Student
from model.Studying import Studying
from model.Subject import Subject
from model.Subtheme import Subtheme
from model.Syllabus import Syllabus
from model.Teacher import Teacher
from model.Topic import Topic

db.bind(provider="sqlite",filename="base", create_db=True)
db.generate_mapping(create_tables=True)
with db_session:
    """Направление"""
    direction1 = Direction(name_direction="Физмат")

    """----------------------------------------------------------------------"""
    """Учебный план"""
    syllabus1 = Syllabus(start='2019', finish='2020')
    print("Учебный план:", syllabus1)
    print("----------------------------------------------------------------------")
    """----------------------------------------------------------------------"""
    """Класс"""
    klass1 = Klas(date_set=datetime(2013, 9, 1), letter="a", direction=direction1, syllabus=syllabus1)
    klass1.get_number_today()


    """----------------------------------------------------------------------"""
    """Ученики"""
    student1 = Student(date=datetime(2006, 7, 16), first_name="Коваль", second_name="Александр", patronymic="Викторович")
    student2 = Student(date=datetime(2006, 8, 10), first_name="Чебыкин", second_name="Роман", patronymic="Сергеевич")
    klass1.add_student(student1)
    klass1.add_student(student2)
    print("Класс",klass1.get_number_today(), klass1.get_letter())
    print(klass1)
    print("----------------------------------------------------------------------")

    """----------------------------------------------------------------------"""
    """Учителя"""
    teacher1 = Teacher(first_name="Иванова", second_name="Мария", patronymic="Петровна")
    teacher2 = Teacher(first_name="Гунёва", second_name="Раисия", patronymic="Петровна")

    """----------------------------------------------------------------------"""
    """Предметы"""
    subject1 = Subject(item_name="Математика", teacher=teacher1)
    subject2 = Subject(item_name="Биология", teacher=teacher2)
    """----------------------------------------------------------------------"""
    """Темы занятий"""
    topic1 = Topic(name_topic="Дроби")
    topic2 = Topic(name_topic="Рациональные числа")
    topic3 = Topic(name_topic="Анатомия человека")
    topic4 = Topic(name_topic="Физиология человека")

    """----------------------------------------------------------------------"""
    """Изучается"""
    studying1 = Studying(hour=2, klas=klass1, syllabus=syllabus1, subject=subject1, teacher=teacher1)
    sub_topic = Subtheme(studying=studying1, topic=topic1)
    sub_topic1 = Subtheme(studying=studying1, topic=topic2)
    sub_topic2 = Subtheme(studying=studying1, topic=topic3)
    sub_topic3 = Subtheme(studying=studying1, topic=topic4)
    studying1.get_sub_themes().extend([sub_topic, sub_topic1, sub_topic2, sub_topic3])
    print(studying1)
    print("----------------------------------------------------------------------")
    """----------------------------------------------------------------------"""
    """Результат"""

    result1 = Result(mark=5,datemark=datetime(2013,9,2),student=student1,topic=topic1)
    result2 = Result(mark=4,datemark=datetime(2013,9,19),student=student2,topic=topic3)
    print(result1)
    print(result2)