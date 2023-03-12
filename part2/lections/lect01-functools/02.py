# filter map reduce

t = open("./01.txt").readlines()
t = list(map(int, t))

def q(x): return -x
t = list(map(q, t))

t = list(map(lambda x: -x, t))
print(t)

# ['12\n', '34\n', '-111\n', '55\n', '66\n', '65\n', '99\n', '10\n']  