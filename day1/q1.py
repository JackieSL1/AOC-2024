import sys

l1 = []
l2 = []

with open(sys.argv[1]) as f:
    for line in f:
        item1, item2 = line.rstrip("\n").split("  ")

        l1.append(int(item1))
        l2.append(int(item2))

l1.sort()
l2.sort()

result = 0
for item1, item2 in zip(l1, l2):
    result += abs(item2 - item1)

print(result)
