import sys
from collections import defaultdict

rules = defaultdict(list)
numbers = []

input_file = sys.argv[1]
with open(input_file) as f:
    for line in f:
        if line == "\n":
            break

        num1, num2 = line.rstrip().split("|")
        print(num1, num2)
        rules[int(num1)].append(int(num2))

    for line in f:
        numbers.append([int(num) for num in line.rstrip().split(",")])

def print_queue(rules: defaultdict[int, list[int]], numbers: list[list[int]]) -> int:
    result = 0
    for row in numbers:
        if valid_line(rules, row):
            continue

        print(row)
        row = order_row(rules, row)
        print(row)
        print()
        result += row[len(row) // 2]

    return result

def valid_line(rules: defaultdict[int, list[int]], number_row: list[int]) -> bool:
    indices = dict()
    for i, num in enumerate(number_row):
        indices[num] = i

    for leading_num, other_nums in rules.items():
        for num in other_nums:
            if num in indices and leading_num in indices and indices[num] < indices[leading_num]:
                return False

    return True

def order_row(rules: defaultdict[int, list[int]], number_row: list[int]) -> list[int]:
    i = 0
    while i < len(number_row) - 1:
        num1 = number_row[i]
        num2 = number_row[i + 1]

        if num1 in rules[num2]:
            number_row[i] = num2
            number_row[i + 1] = num1
            i = 0
        else:
            i += 1

    return number_row

print(f"{print_queue(rules, numbers)=}")
