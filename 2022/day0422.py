import re

with open("input0422.txt") as file:
    data = file.readlines()


def part1(array):
    result = 0
    for reading in array:
        a, b, c, d = re.findall('[0-9]+', reading)
        if eval(f"{a} < {c}") and eval(f"{b} < {d}"):
            continue
        elif eval(f"{a} > {c}") and eval(f"{b} > {d}"):
            continue
        else:
            result += 1
    return result


print(part1(data))