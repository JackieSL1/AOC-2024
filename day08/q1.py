import sys
from collections import defaultdict

filename = sys.argv[1]
input: defaultdict[str, set[tuple[int, int]]] = defaultdict(set)
with open(filename) as f:
    for y, line in enumerate(f):
        for x, freq in enumerate(line.rstrip()):
            if freq != '.':
                input[freq].add((x, y))

    max_x = x + 1
    max_y = y + 1

def get_antinodes(frequences: defaultdict[str, set[tuple[int, int]]], max_x: int, max_y: int) -> set:
    antinodes = set()

    for freqs in frequences.values():
        for x1, y1 in freqs:
            for x2, y2 in freqs:
                x_diff = x2 - x1
                y_diff = y2 - y1

                if x_diff == 0 and y_diff == 0:
                    continue

                i = 0
                while True:
                    node = (x1 + x_diff*i, y1 + y_diff*i)
                    # if (node[0], node[1]) in ((x1, y1), (x2, y2)):
                    #     continue

                    if not (0 <= node[0] <+ max_x and 0 <= node[1] < max_y):
                        break

                    antinodes.add(node)
                    i += 1

                i = 0
                while True:
                    node = (x1 - x_diff*i, y1 - y_diff*i)
                    # if (node[0], node[1]) in ((x1, y1), (x2, y2)):
                    #     continue

                    if not (0 <= node[0] <+ max_x and 0 <= node[1] < max_y):
                        break

                    antinodes.add(node)
                    i += 1

    return antinodes

antinodes = get_antinodes(input, max_x, max_y)
with open(filename) as f:
    for y, line in enumerate(f):
        for x, freq in enumerate(line.rstrip()):
            if (x, y) in antinodes and freq == ".":
                print("#", end="")
            else:
                print(freq, end="")
        print("\n")

print(antinodes)
print(f"{len(antinodes)}")
