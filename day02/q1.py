import sys

def safe_reports(reports: list[list[int]]) -> int:
    result = 0

    for report in reports:
        if report[0] == report[1]:
            continue

        increasing = report[0] < report[1]
        for i, _ in enumerate(report):
            if i == len(report) - 1:
                result += 1
                break

            diff = abs(report[i] - report[i+1])
            if diff < 1 or diff > 3:
                break

            if increasing and report[i] >= report[i+1]:
                break
            if not increasing and report[i] <= report[i+1]:
                break

    return result


filename = sys.argv[1]
with open(filename) as input:
    reports = [list(map(int, line.strip().split(" "))) for line in input]

print(safe_reports(reports))
