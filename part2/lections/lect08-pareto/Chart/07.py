import matplotlib.pyplot as plt
from random import randint as rnd

"""
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
"""

def get_a():
    x = list(range(2, 12+1))
    pairs = [rnd(1,6) + rnd(1,6) for _ in range(1000)]
    y = [pairs.count(num) for num in x]
    return x, y

def get_b():
    x = list(range(1, 6+1))
    lst = [rnd(1,6) for _ in range(600)]
    y = [lst.count(num) for num in x]
    return x, y


print(plt.style.available)
plt.style.use('bmh')


fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(12,8), dpi=80)
# fig.set_figwidth(5)  # ширина окна
# fig.set_figheight(6)  # высота окна

x, y = get_a()
ax1.scatter(x, y, label='pair cubes')
ax1.legend()

x, y = get_b()
ax2.scatter(x, y, label='one cube')
ax2.legend()

# steps_y = [step for step in range(min(y)//10*10-10, max(y)//10*10+20, 10)]
# ax2.set_yticks(steps_y)


ax3.bar(x, y, width=1, edgecolor="white", linewidth=0.7, label='one cube - bar')
# ax2.set_yticks([100, 120, 140, 150, 160, 180, 200])
ax3.legend()

plt.show()
