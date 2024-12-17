def operators(totals: dict[int, list[int]]):
    return sum(total for total, nums in totals.items() if (total in find_sum_or_prod(nums)))


def find_sum_or_prod(nums: list[int]) -> list[int]:
    if len(nums) == 2:
        r = [sum(nums), nums[0] * nums[1], int(str(nums[1]) + str(nums[0]))]
        return r

    return [nums[0] * num for num in find_sum_or_prod(nums[1:])] \
        + [nums[0] + num for num in find_sum_or_prod(nums[1:]) ] \
        + [int(str(num) + str(nums[0])) for num in find_sum_or_prod(nums[1:]) ]


with open("test_input.txt") as file:
    test_totals = {
        int(key): list(reversed([int(v) for v in value.strip().split(" ")]))
        for key, value in (line.rstrip().split(':') for line in file)
    }

# print(f"{operators(test_totals)=}")
# print(f"{operators(test_totals)==11387=}")
# print(f"{find_sum_or_prod([15, 6, 8, 6])}")

with open("input.txt") as file:
    totals = {
        int(key): list(reversed([int(v) for v in value.strip().split(" ")]))
        for key, value in (line.rstrip().split(':') for line in file)
    }
print(operators(totals))
