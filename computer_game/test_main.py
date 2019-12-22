from unittest import TestCase
from computer_game.main import *


class Test(TestCase):
    def test_count_good_solutions(self):
        test_set_3 = [
            Door(1, DoorType.MONSTER, 40),
            Door(2, DoorType.ARTIFACT, 20),
            Door(3, DoorType.MONSTER, 25),
            Door(4, DoorType.MONSTER, 20)
        ]
        print_doors(get_greedy_solution(test_set_3))
        print(count_good_solutions(test_set_3))