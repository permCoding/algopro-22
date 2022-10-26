from os import system


def get_lines(name_file):
    f = open(name_file)
    lines = []
    for line in f:
        lines.append(line.strip())
    f.close()
    return lines


def get_sum_odd(line):
    return sum([int(x) for x in line.strip().split() if int(x)%2 > 0])


def write_lines(lines):
    f = open("./data/_01.txt", mode='w', encoding="utf-8")
    for line in lines:
        f.write(f"{get_sum_odd(line)} - {line}\n")
    f.close()


system("cls")

lines = get_lines("./data/01.txt")
write_lines(lines)
