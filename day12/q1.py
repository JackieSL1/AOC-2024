from collections import deque
from enum import Enum
import sys

'''
Use a hashmap to represent the regions: The key is the (x, y), and the value is the crop.

For each x, y, perform a graph search to find the area of a region.
The perimeter will be the number edges connected to a different region, which we can stop search at.

Once a region is fully search, we can add the product of the area and permieter to a result

During graph search, add plots part of that region
to a visited set to avoid visiting them twice.
These can also be skipped during the x,y iteration

'''
type point = tuple[int, int]
class Direction(Enum):
    NORTH = (0, 1)
    SOUTH = (0, -1)
    EAST = (1, 0)
    WEST = (-1, 0)

directions = [dir.value for dir in Direction]

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

    while len(to_visit) != 0:
        next = to_visit.pop()
        print(next)

        for dir in directions:
            plot = (next[0] + dir[0], next[1] + dir[1])

            if plot in visited_plots:
                continue
            elif not within_bounds(plot) or regions[plot] != crop:
                perimeter += 1
            else:
                to_visit.appendleft(plot)
                visited_plots.add(plot)
                visited.add(plot)

        area += 1

    print(f"{area=}")
    print(f"{perimeter=}")
    return area * perimeter

def within_bounds(p: point) -> bool:
    x, y = p
    return 0 <= x < max_x and 0 <= y < max_y

print(f"{get_farm_price()=}")
