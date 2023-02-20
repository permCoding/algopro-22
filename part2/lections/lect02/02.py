from functools import reduce 

file = open("./abitura.csv",'r',encoding='utf8')
t = file.readlines()[1:]
m = map(lambda s: s.split(','), t)
m = map(lambda e: (e[1],int(e[2]),int(e[3])), m)
r = sorted(list(m), key=lambda e: (e[1], -e[2]))
print(r)

[
    ('Коленька', 18, 201), 
    ('Гоген', 18, 201), 
    ('Алекс', 18, 197), 
    ('Саша', 18, 197), 
    ('Саня', 19, 235), 
    ('Стас', 19, 235), 
    ('Митя', 19, 182)
]