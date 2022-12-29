import string

lowercase_priority = dict(zip(string.ascii_lowercase, range(1, 27)))
uppercase_priority = dict(zip(string.ascii_uppercase, range(27, 53)))
priority = {**lowercase_priority, **uppercase_priority}


"""def common_item(string1, string2):
    return ''.join(set(string1).intersection(string2))"""


def common_item(*args):
    string1, *string2 = args
    if len(string2) < 2:
        return ''.join(set(string1).intersection(string2[0]))
    return ''.join(set(string1).intersection(string2[0], string2[1]))


def part1(data):
    sum_priority = 0
    for rucksack in data:
        length = len(rucksack)
        mid_point = int(length/2)
        first_compartment, second_compartment = rucksack[:mid_point], rucksack[mid_point:]
        common_list = common_item(first_compartment, second_compartment)
        sum_priority += priority[common_list]
    return sum_priority


def part2(data):
    sum_priority = 0
    three_rucksacks = [array[index:index+3] for index in range(0, len(array), 3)]
    for three_rucksack in three_rucksacks:
        common_list = common_item(three_rucksack[0], three_rucksack[1], three_rucksack[2])
        sum_priority += priority[common_list]
    return sum_priority


with open("input0322.txt") as file:
    array = file.read().split("\n")

print(part1(array))  # 8349
print(part2(array))  # 2681
