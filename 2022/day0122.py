
def part1(array):
    max_calories = 0
    for elf in array:
        sum_calories = sum(elf)
        if sum_calories >= max_calories:
            max_calories = sum_calories
    return max_calories

def part2(array):
    calories_array = sorted([sum(elf) for elf in array])
    return sum(calories_array[-3:])


with open("input01_22.txt") as file:
    data = file.read().split("\n\n")
    elves = [list(map(lambda datapoint: int(datapoint), elf.split("\n"))) for elf in data]

print(part1(elves))
print(part2(elves))


