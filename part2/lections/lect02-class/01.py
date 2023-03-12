from functools import reduce 

file = open("./abitura.csv",'r',encoding='utf8')
t = file.readlines()[1:]
m = map(lambda s: s.split(','), t)
m = map(lambda e: (e[1],int(e[2]),int(e[3])), m)
f = list(filter(lambda e: e[1]==19, m))
f.sort(key=lambda e: e[2], reverse=True)
print(f)

[
    ('Саня', 19, 235), 
    ('Стас', 19, 235), 
    ('Митя', 19, 182)
]