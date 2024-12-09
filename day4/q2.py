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
            if letter == "A":
                search_diffs = (
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1),
                )
                count = 0
                for x_diff, y_diff in search_diffs:
                    if search(word_search, x, y, x_diff, y_diff):
                        count += 1
                    if count >= 2:
                        result += 1
                        break


    return result

def search(word_search: list[str], x: int, y: int, x_diff: int, y_diff: int) -> bool:
    if not (0 <= y + y_diff < len(word_search)): return False
    if not (0 <= y - y_diff < len(word_search)): return False
    if not (0 <= x + x_diff < len(word_search)): return False
    if not (0 <= x - x_diff < len(word_search)): return False

    return word_search[y - y_diff][x - x_diff] == "M" \
            and word_search[y + y_diff][x + x_diff] == "S"

print(find_xmas(word_search))
