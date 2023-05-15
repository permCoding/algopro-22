import matplotlib.pyplot as plt


lst = [
    (4, 125, 970),
    (5, 128, 980),
    (13, 132, 1060),
    (18, 130, 1050),
    (12, 130, 1060),
    (18, 130, 1080),
    (19, 128, 1095),
    (16, 120, 1099),
    (17, 125, 1090),
    (9, 120, 1050),
    (10, 120, 1065),
    (11, 125, 1055),
    (3, 120, 999),
]
x = [e[1] for e in lst[:4]]
y = [e[2] for e in lst[:4]]
plt.scatter(x, y, c='green')
 
x = [e[1] for e in lst[4:]]
y = [e[2] for e in lst[4:]]
plt.scatter(x, y, c='red')

plt.show()
