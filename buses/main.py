from enum import IntEnum
from typing import List
from typing import Dict
import json


class BusType(IntEnum):
    BIG = 0,
    MEDIUM = 1,
    SMALL = 2


class BusStop:
    def __init__(self, stop_id: int, name: str):
        self.id = stop_id
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, BusStop):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


class Route:
    def __init__(self, route_id: int, bus_type: BusType, stops_list: List[BusStop], bus_number: int,
                 department_id: int):
        self.id = route_id
        self.bus_type = bus_type
        self.stop_list = stops_list
        self.bus_number = bus_number
        self.department_id = department_id

    def __eq__(self, other):
        if not isinstance(other, Route):
            return NotImplemented
        return self.id == other.id and self.department_id == other.department_id and self.bus_type == other.bus_type

    def __hash__(self):
        return hash((self.id, self.department_id, self.bus_type))


def get_total_bus_number(routes: List[Route]) -> int:
    """Returns sum of amounts of buses in routes."""
    return sum(map(lambda route: route.bus_number, routes))


def get_stop_routes(stop: BusStop, all_routes: List[Route]) -> List[Route]:
    """Returns all routes passing given stop."""
    return list(filter(lambda route: stop in route.stop_list, all_routes))


def get_department_routes(department_id: int, all_routes: List[Route]) -> List[Route]:
    """Get all routes belonging to given department."""
    return list(filter(lambda route: route.department_id == department_id, all_routes))


def get_route_stop_list(route_id: int, all_routes: List[Route]) -> List[BusStop]:
    """Finds route in given list and returns it way."""
    return [stop for route in filter(lambda route: route.id == route_id, all_routes) for stop in route.stop_list]


def get_routes_from_file(path_to_file: str) -> List[Route]:
    """Reads list of routes from file."""
    file = open(path_to_file, 'r')
    result = [__route_from_dict(json.loads(line)) for line in
              file.readlines()]
    file.close()
    return result


def write_routes_to_file(path_to_file: str, routes: List[Route]) -> None:
    """Write given routes list to file."""
    file = open(path_to_file, 'w')
    for route in routes:
        print(json.dumps(route, default=lambda r: getattr(r, '__dict__', str(r))), file=file)
    file.close()


def __stop_from_dict(data: Dict) -> BusStop:
    return BusStop(
        data.get("id"),
        data.get("name")
    )


def __route_from_dict(data: Dict) -> Route:
    return Route(
        data.get("id"),
        BusType(data.get("bus_type")),
        [__stop_from_dict(stop_dict) for stop_dict in data.get("stop_list")],
        data.get("bus_number"),
        data.get("department_id")
    )


def print_routes(routes: List[Route]) -> None:
    print("| id|dep| type |num|")
    for route in routes:
        print(
            "|{0:03d}|{1:03d}|{2:>6s}|{3:>03d}|".format(
                route.id,
                route.department_id,
                route.bus_type.name,
                route.bus_number
            )
        )


def print_stops(stops: List[BusStop]) -> None:
    for stop in stops:
        print("{}".format(stop.id, stop.name))


def main():
    routes = get_routes_from_file("resources/test/bus.dat")
    print("Read routes:")
    print_routes(routes)
    print("Total bus number: {:d}.".format(get_total_bus_number(routes)))


if __name__ == '__main__':
    main()
