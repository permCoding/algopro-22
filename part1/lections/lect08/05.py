from os import system


def get_line(name_file, num_line=0):
    f = open(name_file)
    line = f.readlines()
    f.close()
    return line[num_line]


def get_sum_odd(line):
    return sum([int(x) for x in line.strip().split() if int(x)%2 > 0])


system("cls")

line = get_line("./data/01.txt", 2)
print(line)
print(get_sum_odd(line))
