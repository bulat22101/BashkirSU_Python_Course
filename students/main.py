from typing import List
from typing import Dict
import statistics
import datetime


class Professor:
    def __init__(self, name: str):
        self.name = name


class Discipline:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class Grade:
    def __init__(self, discipline: Discipline, professor: Professor, value: int):
        self.discipline = discipline
        self.professor = professor
        self.value = value


class Student:
    def __init__(self, name: str, birth_date: datetime.date, study_year: int, group_number: int,
                 grades: List[Grade]):
        self.name = name
        self.birth_date = birth_date
        self.study_year = study_year
        self.group_number = group_number
        self.grades = grades

    def __repr__(self):
        return self.name


def get_students_per_course(students: List[Student]) -> List[List[Student]]:
    courses = [[] for i in range(7)]
    for student in students:
        courses[student.study_year].append(student)
    for course in courses:
        course.sort(key=lambda s: s.name)
    return courses


def get_oldest_student(students: List[Student]) -> Student:
    return min(students, key=lambda student: student.birth_date)


def get_youngest_student(students: List[Student]) -> Student:
    return max(students, key=lambda student: student.birth_date)


def get_students_by_groups(students: List[Student]) -> Dict[int, List[Student]]:
    result = dict()
    for student in students:
        result.setdefault(student.group_number, []).append(student)
    return result


def get_grades_by_discipline(grades: List[Grade]):
    result = dict()
    for grade in grades:
        result.setdefault(grade.discipline, []).append(grade)
    return result


def get_average_grade_by_discipline_in_groups(students: List[Student]):
    students_by_groups = get_students_by_groups(students)
    result = dict()
    for group in students_by_groups:
        students_in_group = students_by_groups[group]
        group_grades = [grade for student in students_in_group for grade in student.grades]
        group_grades_by_discipline = get_grades_by_discipline(group_grades)
        average_group_grades = dict(
            [
                (discipline, statistics.mean(map(lambda grade: grade.value, group_grades_by_discipline[discipline])))
                for discipline in group_grades_by_discipline
            ]
        )
        result.update([(group, average_group_grades)])
    return result


def get_student_with_max_grade_by_group(students: List[Student]):
    students_by_groups = get_students_by_groups(students)
    return dict(
        [
            (
                group,
                max(students_by_groups[group], key=lambda student: sum(map(lambda grade: grade.value, student.grades)))
            )
            for group in students_by_groups
        ]
    )


if __name__ == '__main__':
    pass
