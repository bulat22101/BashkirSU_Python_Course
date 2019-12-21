import unittest
from datetime import date

from students.main import *


class Test(unittest.TestCase):
    def setUp(self):
        self.professor1 = Professor("John Smith")
        self.professor2 = Professor("Ivan Ivanov")
        self.discipline1 = Discipline("English")
        self.discipline2 = Discipline("Russian")
        self.discipline3 = Discipline("Computer Science")
        self.grades = [
            Grade(self.discipline1, self.professor1, 85),
            Grade(self.discipline2, self.professor2, 45),
            Grade(self.discipline3, self.professor1, 72),
            Grade(self.discipline1, self.professor1, 49),
            Grade(self.discipline2, self.professor2, 32),
            Grade(self.discipline3, self.professor1, 112),
            Grade(self.discipline1, self.professor1, 79),
            Grade(self.discipline2, self.professor2, 64),
            Grade(self.discipline3, self.professor1, 92),
            Grade(self.discipline1, self.professor1, 34),
            Grade(self.discipline2, self.professor2, 57),
            Grade(self.discipline3, self.professor1, 43),
            Grade(self.discipline1, self.professor1, 46),
            Grade(self.discipline2, self.professor2, 51),
            Grade(self.discipline3, self.professor1, 84)
        ]
        self.students = [
            Student("Vasiliy Kozlov", date(1997, 12, 23), 1, 14, [self.grades[0], self.grades[1], self.grades[2]]),
            Student("Ivan Ivanov", date(1995, 2, 13), 2, 23, [self.grades[3], self.grades[4], self.grades[5]]),
            Student("Vasiliy Bunin", date(1996, 9, 30), 1, 13, [self.grades[6], self.grades[7], self.grades[8]]),
            Student("Peter Brown", date(1994, 7, 17), 2, 23, [self.grades[9], self.grades[10], self.grades[11]]),
            Student("James Bond", date(1993, 5, 4), 2, 23, [self.grades[12], self.grades[13], self.grades[14]])
        ]

    def test_get_student_per_course(self):
        expected = [
            [],
            [self.students[2], self.students[0]],
            [self.students[1], self.students[4], self.students[3]],
            [],
            [],
            [],
            []
        ]
        self.assertEqual(expected, get_students_per_course(self.students))

    def test_get_oldest_student(self):
        self.assertEqual(self.students[4], get_oldest_student(self.students))

    def test_get_youngest_student(self):
        self.assertEqual(self.students[0], get_youngest_student(self.students))

    def test_get_students_by_groups(self):
        expected = {
            13: [self.students[2]],
            14: [self.students[0]],
            23: [self.students[1], self.students[3], self.students[4]]
        }
        self.assertEqual(expected, get_students_by_groups(self.students))

    def test_get_average_grade_by_discipline_in_groups(self):
        expected = {
            13: {
                self.discipline1: self.grades[6].value,
                self.discipline2: self.grades[7].value,
                self.discipline3: self.grades[8].value
            },
            14: {
                self.discipline1: self.grades[0].value,
                self.discipline2: self.grades[1].value,
                self.discipline3: self.grades[2].value
            },
            23: {
                self.discipline1: (self.grades[3].value + self.grades[9].value + self.grades[12].value) / 3,
                self.discipline2: (self.grades[4].value + self.grades[10].value + self.grades[13].value) / 3,
                self.discipline3: (self.grades[5].value + self.grades[11].value + self.grades[14].value) / 3,
            }
        }
        self.assertEqual(expected, get_average_grade_by_discipline_in_groups(self.students))

    def test_get_student_with_max_grade_by_group(self):
        expected = {
            13: self.students[2],
            14: self.students[0],
            23: self.students[1]
        }
        self.assertEqual(expected, get_student_with_max_grade_by_group(self.students))


if __name__ == '__main__':
    unittest.main()
