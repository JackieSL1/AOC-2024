from ast import match_case
from os import dup
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
    time_loops = set()
    heading = (0, -1) # Heading upwards
    ups = set()
    rights = set()
    downs = set()
    lefts = set()

    while True:
        new_location = (location[0] + heading[0], location[1] + heading[1])

        if new_location in obstacles:
            heading = rotate_right(heading)
            continue

        if not (0 < new_location[0] < max_x and 0 < new_location[1] < max_y):
            break

        match heading:
            case (0, -1):
                ups.update(get_path(new_location, obstacles, max_x, max_y, heading))
                if new_location in rights:
                    time_loops.add(new_location)
            case (1, 0):
                rights.update(get_path(new_location, obstacles, max_x, max_y, heading))
                if new_location in downs:
                    time_loops.add(new_location)
            case (0, 1):
                downs.update(get_path(new_location, obstacles, max_x, max_y, heading))
                if new_location in lefts:
                    time_loops.add(new_location)
            case (-1, 0):
                lefts.update(get_path(new_location, obstacles, max_x, max_y, heading))
                if new_location in ups:
                    time_loops.add(new_location)

        positions.add(new_location)
        location = new_location

    with open(input_file) as f:
        for y, line in enumerate(f):
            for x, item in enumerate(line.rstrip()):
                if (x,y) in time_loops:
                    item = "O"
                elif (x,y) in ups:
                    item = "X"
                print(item, end="")
            print()

    print(time_loops)
    return len(time_loops)

def get_path(location: point, obstacles: set[point], max_x: int, max_y: int, heading: point) -> list[point]:
    result = []
    i = 0
    if heading[0] != 0:
        while 0 <= location[0] + i < max_x and (location[0] + i, location[1]) not in obstacles:
            result.append((location[0] + i, location[1]))
            i += 1

        i = 0
        while 0 <= location[0] - i < max_x and (location[0] - i, location[1]) not in obstacles:
            result.append((location[0] - i, location[1]))
            i += 1
    else:
        while 0 <= location[1] + i < max_y and (location[0], location[1] + i) not in obstacles:
            result.append((location[0], location[1] + i))
            i += 1

        i = 0
        while 0 <= location[1] - i < max_y and (location[0], location[1] - i) not in obstacles:
            result.append((location[0], location[1] - i))
            i += 1

    # print(result)
    # sys.exit()
    return result

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
