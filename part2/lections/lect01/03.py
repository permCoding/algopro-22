# filter map reduce

t = list(map(int, open("./01.txt").readlines()))

f = list(filter(lambda x: x<0, t))

print(f)
