import unittest

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
        self.assertEqual(
            [[], [self.students[2], self.students[0]], [self.students[1], self.students[4], self.students[3]], [], [],
             [], []],
            get_students_per_course(self.students))

    def test_get_oldest_student(self):
        self.assertEqual(self.students[4], get_oldest_student(self.students))

    def test_get_youngest_student(self):
        self.assertEqual(self.students[0], get_youngest_student(self.students))




if __name__ == '__main__':
    unittest.main()
