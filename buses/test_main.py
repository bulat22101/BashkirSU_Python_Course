import unittest
import json
from buses.main import *


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.bus_stops = [
            BusStop(1, "Golders Green Station"),
            BusStop(2, "Waterloo Station"),
            BusStop(3, "Lancaster Place"),
            BusStop(4, "Trafalgar Square"),
            BusStop(5, "Selfridges"),
            BusStop(6, "Oxford Street"),
            BusStop(7, "Baker Street"),
            BusStop(8, "Frampton Street"),
            BusStop(9, "Marlborough Place"),
            BusStop(10, "West End Lane")
        ]
        self.routes = [
            Route(
                1,
                BusType.BIG,
                [self.bus_stops[0], self.bus_stops[3], self.bus_stops[7], self.bus_stops[9]],
                12,
                1
            ),
            Route(
                2,
                BusType.SMALL,
                [self.bus_stops[1], self.bus_stops[3], self.bus_stops[5], self.bus_stops[8], self.bus_stops[9]],
                52,
                2
            ),
            Route(
                3,
                BusType.MEDIUM,
                [self.bus_stops[2], self.bus_stops[3], self.bus_stops[4], self.bus_stops[5]],
                72,
                1
            ),
            Route(
                4,
                BusType.BIG,
                [self.bus_stops[0], self.bus_stops[1], self.bus_stops[6], self.bus_stops[9]],
                1,
                3
            ),
        ]

    def test_get_total_bus_number(self):
        self.assertEqual(137, get_total_bus_number(self.routes))
        self.assertEqual(125, get_total_bus_number(self.routes[1:]))

    def test_get_stop_routes(self):
        stop1 = self.bus_stops[9]
        expected1 = {self.routes[0], self.routes[1], self.routes[3]}
        self.assertEqual(expected1, set(get_stop_routes(stop1, self.routes)))
        stop2 = self.bus_stops[6]
        expected2 = [self.routes[3]]
        self.assertEqual(expected2, get_stop_routes(stop2, self.routes))

    def test_get_department_routes(self):
        department1 = 1
        expected1 = {self.routes[0], self.routes[2]}
        self.assertEqual(expected1, set(get_department_routes(department1, self.routes)))
        department2 = 2
        expected2 = [self.routes[1]]
        self.assertEqual(expected2, get_department_routes(department2, self.routes))

    def test_get_routes_from_file(self):
        self.assertEqual(self.routes, get_routes_from_file("resources/test/bus.dat"))

    def test_write_read(self):
        file_path = "resources/test/temp_test.dat"
        write_routes_to_file(file_path, self.routes)
        read_routes = get_routes_from_file(file_path)
        self.assertEqual(self.routes, read_routes)