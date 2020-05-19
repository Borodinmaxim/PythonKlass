from datetime import datetime

from python.direction import Direction
from python.klas import Klas
from python.result import Result
from python.student import Student
from python.studying import Studying
from python.subject import Subject
from python.subtheme import Subtheme
from python.syllabus import Syllabus
from python.teacher import Teacher
from python.topic import Topic


"""Направление"""
direction1 = Direction(name_direction="Физмат")

"""----------------------------------------------------------------------"""
"""Учебный план"""
syllabus1 = Syllabus(start=2019, finish=2020)
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
studying1 = Studying(2, klass1, syllabus1, subject1, teacher1)
sub_topic = Subtheme(studying1, topic1)
sub_topic1 = Subtheme(studying1, topic2)
sub_topic2 = Subtheme(studying1, topic3)
sub_topic3 = Subtheme(studying1, topic4)
studying1.get_sub_themes().extend([sub_topic, sub_topic1, sub_topic2, sub_topic3])
print(studying1)
print("----------------------------------------------------------------------")
"""----------------------------------------------------------------------"""
"""Результат"""

result1 = Result(5,datetime(2013,9,2),student1,topic1)
result2 = Result(4,datetime(2013,9,19),student2,topic3)
print(result1)
print(result2)