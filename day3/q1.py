import sys
import re

filename = sys.argv[1]

with open(filename) as f:
    input = "".join([line for line in f])

def multiplies(string: str) -> int:
    result = re.findall(r"mul\((\d+),(\d+)\)", string)
    return sum([int(pair[0]) * int(pair[1]) for pair in result])

print(f"{multiplies(input)=}")
