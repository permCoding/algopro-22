import matplotlib.pyplot as plt
from random import randint as rnd


def get():
    return rnd(1,6) + rnd(1,6)


fig, ax = plt.subplots()
x = list(range(2, 12+1))
pairs = [get() for _ in range(1000)]
y = [pairs.count(num) for num in x]

# цвет в 16-ти-ричной СС и размер радиуса
plt.scatter(x, y, c='#000088', s=3)

ax.set_facecolor('#aaeebb')
ax.set_title('Распределение')

# можно задать пропорцию сторон окна
fig.set_figwidth(8)  # ширина окна
fig.set_figheight(3)  # высота окна

plt.show()
