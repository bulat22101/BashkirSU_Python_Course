from datetime import date
from typing import List


class Professor:
    def __init__(self, name: str):
        self.name = name


class Discipline:
    def __init__(self, name: str):
        self.name = name


class Grade:
    def __init__(self, discipline: Discipline, professor: Professor, value: int):
        self.discipline = discipline
        self.professor = professor
        self.value = value


class Student:
    def __init__(self, name: str, birth_date: date, study_year: int, group_number: int,
                 grades: List[Grade]):
        self.name = name
        self.birth_date = birth_date
        self.study_year = study_year
        self.group_number = group_number
        self.grades = grades

    def __repr__(self):
        return self.name


def get_students_per_course(students: List[Student]):
    courses = [[] for i in range(7)]
    for student in students:
        courses[student.study_year].append(student)
    for course in courses:
        course.sort(key=lambda s: s.name)
    return courses


def get_oldest_student(students: List[Student]):
    return min(students, key=lambda student: student.birth_date)


def get_youngest_student(students: List[Student]):
    return max(students, key=lambda student: student.birth_date)


def get_average_points_in_groups(students: List[Student]):
    result = dict.fromkeys(map(lambda student: student.group_number, students), [])
    return result


if __name__ == '__main__':
    print(get_average_points_in_groups())
    pass
