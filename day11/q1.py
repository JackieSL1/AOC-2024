import sys
from time import time

input_file = sys.argv[1]

with open(input_file) as f:
    stones = [int(stone) for stone in f.readline().split(" ")]

def watch_stones(stones: list[int], blinks: int) -> list[int]:

    for _ in range(blinks):

        i = 0
        while i < len(stones):
            stone = stones[i]
            new_stone = stone

            if stone == 0:
                new_stone = 1
            elif len(str(stone))%2==0:
                stone_str = str(stone)
                left = int(stone_str[:len(stone_str) // 2])
                right = int(stone_str[len(stone_str) // 2:])

                stones.insert(i, left)
                new_stone = right

                i += 1
            else:
                new_stone = stone * 2024

            stones[i] = new_stone
            i += 1


    return stones

t1 = time()
result = len(watch_stones(stones, 30))
t2 = time()
print(f"{result=}")
print(f"{(t2 - t1) * 1000}ms")
