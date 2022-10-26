from os import system


def get_line(name_file, num_line=0):
    f = open(name_file)
    line = f.readline()
    f.close()
    return line


system("cls")

line = get_line("./data/01.txt")
lst_s = line.strip().split()
# lst_n = [int(elm) for elm in lst_s]

# lst_n = map(int, lst_s)  # var 1

# lst_n = map(lambda x: int(x), lst_s)  # var 2

def my_func(x):
    return int(x)
lst_n = map(my_func, lst_s)  # var 3
for elm in lst_n:
    print(elm)
# print(lst_n, list(lst_n))

# lst_sorted = sorted(lst_n)
# print(lst_sorted)