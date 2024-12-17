import sys

filename = sys.argv[1]

word_search = []
with open(filename) as f:
    for line in f:
        word_search.append(line.rstrip())


def find_xmas(word_search: list[str]) -> int:
    result = 0

    for y, line in enumerate(word_search):
        for x, letter in enumerate(line):
            if letter == "X":
                search_diffs = (
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                )
                for x_diff, y_diff in search_diffs:
                    if search(word_search, x, y, x_diff, y_diff):
                        result += 1


    return result

def search(word_search: list[str], x: int, y: int, x_diff: int, y_diff: int) -> bool:
    if not (0 <= y + (y_diff * 3) < len(word_search) and 0 <= x + (x_diff * 3) < len(word_search[0])):
        return False

    return word_search[y + y_diff][x + x_diff] == "M" \
    and word_search[y + (y_diff * 2)][x + (x_diff * 2)] == "A" \
    and word_search[y + (y_diff * 3)][x + (x_diff * 3)] == "S"

print(find_xmas(word_search))
