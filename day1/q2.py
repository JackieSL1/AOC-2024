import sys

left_list = set()
right_list = []

with open(sys.argv[1]) as f:
    for line in f:
        item1, item2 = line.rstrip("\n").split("  ")

        left_list.add(int(item1))
        right_list.append(int(item2))


result = 0
for id in right_list:
    if id in left_list:
        result += id

print(result)
