import locale
from functools import cmp_to_key


def get_records(filename, sep=','):
    abiturs = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            t = line.split(sep)
            abiturs.append([int(t[0]), t[1], int(t[2])])
    return abiturs


abiturs = get_records('abiturs.csv')

locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')
func = cmp_to_key(locale.strcoll)

ab_sorted = sorted(abiturs, key=lambda x: func(x[1]))

for ab in ab_sorted:
    print(*ab)
