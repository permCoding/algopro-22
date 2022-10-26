from os import system


def get_line(name_file, num_line=0):
    f = open(name_file)
    line = f.readline()
    f.close()
    return line


system("cls")

line = get_line("./data/01.txt")
print(line)
# print(line[:-1].split(" "))
lst_s = line.strip().split()
lst_n = [int(elm) for elm in lst_s]
# lst_n = 

print(lst_n)
lst_sorted = sorted(lst_n)
lst_n.sort()
print(lst_n)
print(lst_sorted)

