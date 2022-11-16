def get_lines(file_name):
    with open(file_name, mode='r', encoding='utf8') as f:
        return f.readlines()


def get_tuples(lines):
    lst = []
    for line in lines[1:]:
        tmp = line.split(',')
        lst.append((tmp[1], int(tmp[2])))  # array dict list tuple set
    return lst


def get_tuples_map(lines):
    def func(x):
        return (x.split(',')[1], int(x.split(',')[2]))
    return list(map(func, lines[1:]))


lines = get_lines('./txt/data.txt')
tuples = get_tuples_map(lines)
for elm in sorted(tuples, key=lambda x: x[0]):
    print(elm[0].ljust(9, ' '), elm[1])
