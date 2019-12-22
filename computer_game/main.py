from enum import IntEnum
from typing import List
import random
import math


class DoorType(IntEnum):
    MONSTER = -1,
    ARTIFACT = 1


class Door:
    def __init__(self, door_id: int, door_type: DoorType, value: int):
        self.door_id = door_id
        self.door_type = door_type
        self.value = value

    def __repr__(self):
        return self.door_type.name + " " + str(self.value)


def generate_random_doors(doors_number: int) -> List[Door]:
    result = []
    for i in range(doors_number):
        door_type = random.choice([d_type for d_type in DoorType])
        value = random.randint(5, 100) if door_type == DoorType.MONSTER else random.randint(10, 80)
        result.append(Door(i + 1, door_type, value))
    return result


def count_good_solutions_rec(step: int, power: int, current_door: Door, doors: List[Door], visited: List[bool]) -> int:
    if step > 0:
        if current_door.door_type == DoorType.ARTIFACT:
            power += current_door.value
        elif current_door.value > power:
            return 0
    if step == len(doors):
        return 1
    result = 0
    for i in range(len(doors)):
        next_door = doors[i]
        if not visited[i]:
            visited[i] = True
            result += count_good_solutions_rec(step + 1, power, next_door, doors, visited)
            visited[i] = False
    return result


def count_good_solutions(doors: List[Door]) -> int:
    return count_good_solutions_rec(0, 25, None, doors, [False for door in doors])


def print_doors(doors: List[Door]):
    print("| # | id|   type  | value|")
    for door_i in range(len(doors)):
        print(
            "| {0:02d}| {1:02d}| {2:>8s}|   {3:03d}|".format(
                door_i + 1,
                doors[door_i].door_id,
                doors[door_i].door_type.name,
                doors[door_i].value
            )
        )


def get_greedy_solution(doors: List[Door]):
    sum_of_artifacts_values = sum(
        map(lambda door: door.value, filter(lambda door: door.door_type.value == DoorType.ARTIFACT, doors))
    )
    strongest_monster = min(
        filter(lambda door: door.door_type.value == DoorType.MONSTER, doors),
        key=lambda door: door.door_type.value * door.value
    )
    if 25 + sum_of_artifacts_values < strongest_monster.value:
        return []
    else:
        doors_clone = list(doors)
        doors_clone.sort(key=lambda door: door.door_type.value * door.value, reverse=True)
        return doors_clone


def main():
    while True:
        number_of_doors = int(input("Input number of doors[1-10]: ").strip())
        if number_of_doors < 1 or number_of_doors > 10:
            print("Number of doors should be in range 1-10.")
            continue
        doors_list = generate_random_doors(number_of_doors)
        print("Generated doors:")
        print_doors(doors_list)
        ways_number = math.factorial(number_of_doors)
        good_ways_number = count_good_solutions(doors_list)
        print("Good ways: {}/{}.".format(good_ways_number, ways_number))
        print("Greedy solution:")
        print_doors(get_greedy_solution(doors_list))


if __name__ == '__main__':
    main()
