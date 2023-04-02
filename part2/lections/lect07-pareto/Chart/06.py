import matplotlib.pyplot as plt
from random import randint as rnd


fig, ax = plt.subplots()
x = list(range(2, 12+1))
pairs = [rnd(1,6) + rnd(1,6) for _ in range(1000)]
y = [pairs.count(num) for num in x]

plt.scatter(x, y, 
        c='#eeee00', 
        s=20, 
        linewidths=1, 
        edgecolors='#000000',
        marker='o')

ax.set_facecolor('#aaeebb')
ax.set_title('Распределение')

fig.set_figwidth(5)  # ширина окна
fig.set_figheight(5)  # высота окна

ax.set_xticks(x)
steps_y = [step for step in range(min(y)//10*10, (max(y)//10+1)*10, 10)]
ax.set_yticks(steps_y)

plt.show()
