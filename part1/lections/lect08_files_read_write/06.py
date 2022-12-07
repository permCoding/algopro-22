from os import system


def get_lines(name_file):
    with open(name_file) as f:
        lines = f.readlines()
    # return list(map(lambda line: line.strip(), lines))
    return [line.strip() for line in lines]


def get_sum_odd(line):
    return sum([int(x) for x in line.strip().split() if int(x)%2 > 0])


system("cls")

lines = get_lines("./data/01.txt")
for line in lines:
    print(get_sum_odd(line), '-', line)