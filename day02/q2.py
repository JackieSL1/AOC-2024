import sys

def safe_reports(reports: list[list[int]]) -> int:
    result = 0

    for report in reports:
        safe_result = report_is_safe(report)
        print(report, safe_result)
        if safe_result == True:
            result += 1
            continue

        if any(map(lambda r: report_is_safe(r) == True, safe_result)):
            result += 1

    return result

def report_is_safe(report: list[int]):
    increasing = report[0] < report[1]

    for i, _ in enumerate(report):
        if i == len(report) - 1:
            return True

        diff = abs(report[i] - report[i+1])
        if diff < 1 or diff > 3:
            break

        if increasing and report[i] >= report[i+1]:
            break

        if not increasing and report[i] <= report[i+1]:
            break

    return (
            report[:i] + report[i + 1:],
            report[:i + 1] + report[i + 2:],
            report[:2] + report[1:],
            report[1:],
            )


filename = sys.argv[1]
with open(filename) as input:
    reports = [list(map(int, line.strip().split(" "))) for line in input]

print(safe_reports(reports))
