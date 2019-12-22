from unittest import TestCase
from computer_game.main import *


class Test(TestCase):
    def setUp(self) -> None:
        self.test_set_1 = [
            Door(1, DoorType.MONSTER, 100),
            Door(2, DoorType.ARTIFACT, 80)
        ]
        self.test_set_2 = [
            Door(1, DoorType.ARTIFACT, 40),
            Door(2, DoorType.ARTIFACT, 40),
            Door(3, DoorType.ARTIFACT, 33),
            Door(4, DoorType.MONSTER, 54),
            Door(5, DoorType.ARTIFACT, 21),
            Door(6, DoorType.ARTIFACT, 11),
            Door(7, DoorType.ARTIFACT, 17),
            Door(8, DoorType.MONSTER, 20),
        ]
        self.test_set_3 = [
            Door(1, DoorType.MONSTER, 60),
            Door(2, DoorType.ARTIFACT, 20),
            Door(3, DoorType.MONSTER, 25),
            Door(4, DoorType.MONSTER, 20)
        ]

    def test_count_good_solutions(self):
        self.assertEqual(1, count_good_solutions(25, self.test_set_1))
        self.assertEqual(31296, count_good_solutions(25, self.test_set_2))
        self.assertEqual(0, count_good_solutions(25, self.test_set_3))

    def test_get_greedy_solution(self):
        solution1 = get_greedy_solution(25, self.test_set_1)
        solution2 = get_greedy_solution(25, self.test_set_2)
        self.assertNotEqual([], solution1)
        self.assertNotEqual([], solution2)
        self.assertTrue(self.check_solution(25, solution1))
        self.assertTrue(self.check_solution(25, solution2))
        self.assertEqual([], get_greedy_solution(25, self.test_set_3))

    @staticmethod
    def check_solution(start_power: int, doors: List[Door]) -> bool:
        power = start_power
        for door in doors:
            if door.door_type == DoorType.ARTIFACT:
                power += door.value
            elif door.value > power:
                return False
        return True
