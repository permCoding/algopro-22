# структурные эл-ты класса

class Abit:
    def __init__(self, n, a=17, r=0):  # конструктор
        self.name = n
        self.age = int(a)
        self.rat = int(r)
    def __str__(self):
        return f"{self.name}\t{self.age} {self.rat}"


a = Abit("Коля", 18, 188)
b = Abit("Света")
c = Abit("Оля")
t = [a, b, c]
t[1].rat = 205
for e in t: print(e)
# Коля    18 188
# Света   17 205      
# Оля     17 0    