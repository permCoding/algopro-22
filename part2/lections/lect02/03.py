from functools import reduce 

file = open("./abitura.csv",'r',encoding='utf8')
t = file.readlines()[1:]
m = map(lambda s: s.split(','), t)
t = list(map(lambda e: (e[1],int(e[2]),int(e[3])), m))
sm = reduce(lambda sm, e: sm+e[2], t, 0)
avg = sm / len(t)
print(avg)
for e in filter(lambda e: e[2]>avg, t):
    print(*e)
# Саня 19 235
# Стас 19 235
[
    ('Коленька', 18, 201), 
    ('Гоген', 18, 201), 
    ('Алекс', 18, 197), 
    ('Саша', 18, 197), 
    ('Саня', 19, 235), 
    ('Стас', 19, 235), 
    ('Митя', 19, 182)
]