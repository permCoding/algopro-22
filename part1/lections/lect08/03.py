from os import system


def get_line(name_file, num_line=0):
    f = open(name_file)
    line = f.readline()
    f.close()
    return line


system("cls")

line = get_line("./data/01.txt")
lst_s = line.strip().split()
lst_n = list(map(int, lst_s))
lst_f = list(filter(lambda x: x%2>0, lst_n))
print(lst_f)
print(sum(lst_f))
