import sys

input = sys.argv[1]

def operators(totals: dict[int, list[int]]):
    return sum(total for total, nums in totals.items() if (total in find_sum_or_prod(nums)))


def find_sum_or_prod(nums: list[int]) -> list[int]:
    if len(nums) == 2:
        return [sum(nums), nums[0] * nums[1]]

    return [nums[0] * num for num in find_sum_or_prod(nums[1:])] \
        + [nums[0] + num for num in find_sum_or_prod(nums[1:]) ]




with open(input) as file:
    totals = {
        int(key): list(reversed([int(v) for v in value.strip().split(" ")]))
        for key, value in (line.rstrip().split(':') for line in file)
    }

print(f"{operators(totals)==3749=}")
print(operators(totals))
