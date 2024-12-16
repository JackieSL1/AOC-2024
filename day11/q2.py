import sys
from functools import cache
from time import time
from collections import defaultdict

input_file = sys.argv[1]

with open(input_file) as f:
    stones = [int(stone) for stone in f.readline().split(" ")]

def watch_stones(stones: list[int], blinks: int) -> int:
    return sum(watch_stone(stone, blinks) for stone in stones)


@cache
def watch_stone(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1

    if stone == 0:
        return watch_stone(1, blinks - 1)

    if len(str(stone))%2==0:
        stone_str = str(stone)
        left = int(stone_str[len(stone_str) // 2:])
        right = int(stone_str[:len(stone_str) // 2])

        return watch_stone(left, blinks - 1) + watch_stone(right, blinks - 1)

    return watch_stone(stone * 2024, blinks -1)


# Time BEFORE caching for 35 blinks: 9698ms
# Time AFTER caching for 35 blinks: 7ms
t1 = time()
result = watch_stones(stones, 35)
print(f"{result=}")
t2 = time()
print(f"{(t2 - t1) * 1000}ms")
