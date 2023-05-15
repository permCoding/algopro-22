def get_records(filename, sep=','):
    abiturs = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            t = line.split(sep)
            abiturs.append([int(t[0]), t[1], int(t[2])])
    return abiturs


abiturs = get_records('abiturs.csv')
ab_sorted = sorted(abiturs, key=lambda x: x[1])

for ab in ab_sorted:
    print(*ab)
