# filter map reduce
from functools import reduce

t = list(map(int, open("./01.txt").readlines()))
f = list(filter(lambda x: x<0, t))
s = reduce(lambda acc, cur: acc+cur, f)

print(s)

# [-111, -55, -666] 
