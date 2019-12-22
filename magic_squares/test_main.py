import unittest

from magic_squares.main import *


class Test(unittest.TestCase):
    def test_generate_odd_square(self):
        for size in range(1, 150, 2):
            print(size)
            square = generate_odd_square(size)
            self.check_magic_square(square)
            self.check_associative_square(square)

    def test_generate_double_even_square(self):
        for size in range(4, 150, 4):
            print(size)
            square = generate_double_even_square(size)
            self.check_magic_square(square)
            self.check_associative_square(square)

    def test_generate_single_even_square(self):
        for size in range(6, 150, 4):
            print(size)
            square = generate_single_even_square(size)
            self.check_magic_square(square)

    def test_get_magic_square(self):
        for size in range(3, 200, 1):
            print(size)
            square = get_magic_square(size)
            self.check_magic_square(square)

    def check_semi_magic_square(self, square: List[List[int]]):
        size = len(square)
        expected_sum = self.get_expected_sum(size)
        for row in square:
            self.assertEqual(expected_sum, sum(row))
        for i in range(size):
            self.assertEqual(expected_sum, sum(square[i][j] for j in range(size)))

    def check_magic_square(self, square: List[List[int]]):
        self.check_semi_magic_square(square)
        size = len(square)
        expected_sum = self.get_expected_sum(size)
        self.assertEqual(expected_sum, sum([square[i][i] for i in range(size)]))
        self.assertEqual(expected_sum, sum([square[size - i - 1][size - i - 1] for i in range(size)]))

    def check_associative_square(self, square: List[List[int]]):
        size = len(square)
        expected_sum = (size * size + 1)
        for i in range(size):
            for j in range(size // 2 + size % 2):
                self.assertEqual(expected_sum, square[i][j] + square[size - i - 1][size - j - 1])

    @staticmethod
    def get_expected_sum(size: int):
        return size * (size * size + 1) // 2


if __name__ == '__main__':
    unittest.main()
