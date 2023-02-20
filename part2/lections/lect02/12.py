class Abit:
    def __init__(self, n, a=17, r=0):  # конструктор
        self.name = n
        self.age = int(a)
        self.rat = int(r)
    def __str__(self):
        s = self.name.ljust(12, " ")
        return f"{s}{self.age} {self.rat}"


def get_lst(filename, sep=','):
    file = open(filename,'r',encoding='utf8')
    t = file.readlines()[1:]
    m = map(lambda s: s.split(sep), t)
    return list(map(lambda e: Abit(e[1],e[2],e[3]), m))


t = get_lst("./abitura.csv")
for e in t:  # список объектов
    print(e)
