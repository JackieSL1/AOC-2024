import sys
from collections import defaultdict
from typing import Deque

input_file = sys.argv[1]

map = []

with open(input_file) as f:
    for line in f:
        map.append([int(num) for num in line.rstrip()])

def trailheads(map: list[list[int]]) -> int:
    edges = defaultdict(set)
    trailheads = set()

    for y, _ in enumerate(map):
        for x, score in enumerate(map[y]):
            # Keep track of trailheads to do
            # graph search later
            if map[y][x] == 0:
                trailheads.add((x, y))

            # Check the four adjacent scores, and
            # add an edge if they're exactly 1 more than the
            # score of the current location
            if y > 0 and score == map[y-1][x] - 1:
                edges[(x, y)].add((x, y-1))
            if y < len(map) - 1 and score == map[y+1][x] - 1:
                edges[(x, y)].add((x, y+1))
            if x > 0 and score == map[y][x-1] - 1:
                edges[(x, y)].add((x-1, y))
            if x < len(map[0]) - 1 and score == map[y][x+1] - 1:
                edges[(x, y)].add((x+1, y))


    # Once graph has been built, we can search for all paths
    result = 0

    for head in trailheads:
        deque = Deque()
        deque.append(head)

        visited = set()
        trailends = set()

        while len(deque) != 0:
            next = deque.pop()
            print(next)
            visited.add(next)

            # If the score is 9, we'ved reached the end of a trail
            if map[next[1]][next[0]] == 9:
                trailends.add(next)
                continue

            for node in edges[next]:
                if not node in visited:
                    deque.appendleft(node)

        result += len(trailends)

    return result

print(f"{trailheads(map)=}")
