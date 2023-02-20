class Abit:
    def __init__(self, n, a=17, r=0):  # конструктор
        self.name = n
        self.age = int(a)
        self.rat = int(r)
    def __str__(self):
        s = self.name.ljust(12, " ")
        return f"{s}{self.age} {self.rat}"


file = open("./abitura.csv",'r',encoding='utf8')
t = file.readlines()[1:]
m = map(lambda s: s.split(','), t)
t = list(map(lambda e: Abit(e[1],e[2],e[3]), m))
for e in t:  # список объектов
    print(e)
