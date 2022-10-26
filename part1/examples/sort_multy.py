def get_sorted_01(tbl):
    return sorted(tbl, key=lambda x: (-x[2], x[1]))

def get_sorted_02(tbl):
    from operator import itemgetter as ig
    return sorted(sorted(tbl, key=ig(1), reverse=False), key=ig(2), reverse=True)

def get_avg_ball(tbl):
    from functools import reduce
    return reduce(lambda acc,cur: acc+cur[2], tbl, 0) / len(tbl)

def get_tbl():
    with open("./data.txt", "r", encoding="utf-8") as f:
        tbl = []
        for line in f:
            lst = line.strip().split(',')
            tbl.append([int(lst[0]),lst[1],float(lst[2])])
    return tbl

def write_data(tab):
    with open("./data_sorted.txt", "w", encoding="utf-8") as f:
        for rec in tab:
            f.write(",".join(map(str, rec))+'\n')


tbl = [
    [1,"Алекс",4.4],
    [2,"Николя",4.1],
    [3,"Вероника",4.1],
    [4,"Алекс",3.7],
    [5,"Яна",4.4],
    [6,"Олеся",4.1]
]
tbl = get_tbl()

tbl.sort(key=lambda x: -x[0])
for record in tbl:
    print(record)
print()
for record in get_sorted_01(tbl):
    print(record)
print()
for record in get_sorted_02(tbl):
    print(record)
print(round(get_avg_ball(tbl), 2))
write_data(get_sorted_02(tbl))

