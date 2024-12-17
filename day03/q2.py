import sys
import re

filename = sys.argv[1]

with open(filename) as f:
    input = "".join([line for line in f])

def multiplies(string: str) -> int:
    result = 0

    matches = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", string)
    multiply = True
    for x, y, do, do_not in matches:
        if do:
            multiply = True
        elif do_not:
            multiply = False
        elif multiply:
            result += int(x) * int(y)

    return result

print(f"{multiplies(input)=}")
