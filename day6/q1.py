from ast import match_case
import sys
from types import new_class

input_file = sys.argv[1]

type point = tuple[int, int]
obstacles: set[point] = set()
location: point = (0, 0)
max_x = 0
max_y = 0

with open(input_file) as f:
    for y, line in enumerate(f):
        for x, item in enumerate(line.rstrip()):
            if item == "#":
                obstacles.add((x, y))
            elif item == "^":
                location = (x, y)

max_x = x
max_y = y

def gaurds_path(location: point, obstacles: set[point], max_x: int, max_y: int) -> int:
    positions = {location}
    heading = (0, -1) # Heading upwards

    while True:
        new_location = (location[0] + heading[0], location[1] + heading[1])

        if new_location in obstacles:
            heading = rotate_right(heading)
            continue

        if not (0 < new_location[0] < max_x and 0 < new_location[1] < max_y):
            break


        print(new_location)
        positions.add(new_location)
        location = new_location

    return len(positions) + 1

def rotate_right(heading: point) -> point:
    match heading:
        case (0, -1):
            return (1, 0)
        case (1, 0):
            return (0, 1)
        case (0, 1):
            return (-1, 0)
        case (-1, 0):
            return (0, -1)

    raise ValueError(f"invalid heading: {heading}")

print(f"{gaurds_path(location, obstacles, max_x, max_y)=}")
