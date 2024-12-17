from collections import defaultdict, deque
from enum import Enum
import sys

type point = tuple[int, int]
class Direction(Enum):
    NORTH = (0, 1)
    SOUTH = (0, -1)
    EAST = (1, 0)
    WEST = (-1, 0)

input_file = sys.argv[1]
global regions, max_x, max_y, visited

regions = dict()

# Represent regions as 2D array
with open(input_file) as f:
    for y, line in enumerate(f):
        for x, crop in enumerate(line.rstrip()):
            regions[(x, y)] = crop

max_x = x + 1
max_y = y + 1

visited = set()

def get_farm_price() -> int:
    result = 0
    for x in range(max_x):
        for y in range(max_y):
            if (x,y) in visited:
                continue

            result += get_region_price((x, y))

    return result


def get_region_price(initial_point: point) -> int:
    area = 0
    perimeter = 0

    crop = regions[initial_point]

    visited_plots = {initial_point}
    to_visit = deque([initial_point])

    walls = defaultdict(list)

    while len(to_visit) != 0:
        next = to_visit.pop()

        for dir in Direction:
            plot = (next[0] + dir.value[0], next[1] + dir.value[1])

            if plot in visited_plots:
                continue
            elif not within_bounds(plot) or regions[plot] != crop:
                walls[dir].append(next)
            else:
                to_visit.appendleft(plot)
                visited_plots.add(plot)
                visited.add(plot)

        area += 1

    return area * get_sides(walls)

def within_bounds(p: point) -> bool:
    x, y = p
    return 0 <= x < max_x and 0 <= y < max_y

def get_sides(wall_map: defaultdict[Direction, list[point]]) -> int:
    sides = []

    for dir in Direction:
        walls = wall_map[dir]
        if dir == Direction.EAST or dir == Direction.WEST:
            walls.sort()
            group = [walls[0]]
            # x should be the same, and y 1 different
            for wall in walls[1:]:
                if wall[0] == group[-1][0] and abs(wall[1] - group[-1][1]) == 1:
                    group.append(wall)
                else:
                    sides.append(group)
                    group = [wall]
            sides.append(group)
        else:
            # y should be the same, and x 1 different
            walls.sort(key=lambda p:(p[1], p[0]),reverse=True)
            group = [walls[0]]
            for wall in walls[1:]:
                if wall[1] == group[-1][1] and abs(wall[0] - group[-1][0]) == 1:
                    group.append(wall)
                else:
                    sides.append(group)
                    group = [wall]
            sides.append(group)

    return len(sides)


print(f"{get_farm_price()=}")
