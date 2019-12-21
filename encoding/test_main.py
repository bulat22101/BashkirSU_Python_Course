import unittest

from encoding.main import *


class Test(unittest.TestCase):
    def test_check_message(self):
        good1 = "Привет"
        good2 = "Меня зовут Вася"
        good3 = "Вышел Ёжик из тумана"
        bad1 = "Hi привет"
        bad2 = "Привет, как дела?"
        self.assertTrue(check_message(good1))
        self.assertTrue(check_message(good2))
        self.assertTrue(check_message(good3))
        self.assertFalse(check_message(bad1))
        self.assertFalse(check_message(bad2))

    def test_get_serial_number(self):
        self.assertEqual(1, get_serial_number("а"))
        self.assertEqual(2, get_serial_number("б"))
        self.assertEqual(6, get_serial_number("е"))
        self.assertEqual(7, get_serial_number("ё"))
        self.assertEqual(23, get_serial_number("х"))
        self.assertEqual(33, get_serial_number("я"))
        self.assertEqual(0, get_serial_number(" "))

    def test_encode(self):
        message1 = "СЕРВЕР"
        message2 = "фрукт"
        message3 = "Иван Васильевич"
        expected1 = [1222, 1155, 402]
        expected2 = [1426, 1356, 1280]
        expected3 = [643, 79, 3, 83, 653, 1926, 202, 1600]
        self.assertEqual(expected1, encode_message(message1))
        self.assertEqual(expected2, encode_message(message2))
        self.assertEqual(expected3, encode_message(message3))

    def test_decode(self):
        encoded_sequence1 = [1222, 1155, 402]
        encoded_sequence2 = [1426, 1356, 1280]
        encoded_sequence3 = [643, 79, 3, 83, 653, 1926, 202, 1600]
        expected1 = "СЕРВЕР"
        expected2 = "ФРУКТ "
        expected3 = "ИВАН ВАСИЛЬЕВИЧ "
        self.assertEqual(expected1, decode_message(encoded_sequence1))
        self.assertEqual(expected2, decode_message(encoded_sequence2))
        self.assertEqual(expected3, decode_message(encoded_sequence3))

    def test_integration(self):
        self.assertEqual("СЕРВЕР", decode_message(encode_message("СЕРВЕР")))
        self.assertEqual("ВАСИЛИЙ ", decode_message(encode_message("ВАСИЛИЙ")))
        self.assertEqual("ИВАН ИВАНОВИЧ ", decode_message(encode_message("Иван Иванович")))


if __name__ == '__main__':
    unittest.main()
