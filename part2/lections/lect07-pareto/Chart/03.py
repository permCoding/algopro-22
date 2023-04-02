import matplotlib.pyplot as plt
from random import randint as rnd


def get():
    return rnd(1,6) + rnd(1,6)


x = list(range(2, 12+1))
pairs = [get() for _ in range(1000)]
y = [pairs.count(num) for num in x]
plt.scatter(x, y, c='#000088')  # можно цвет в 16-ти-ричной СС

plt.show()
