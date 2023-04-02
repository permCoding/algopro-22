import matplotlib.pyplot as plt

# colors: {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
# цвета можно писать полными словами: black, ...

x = [1, 2, 3, 4]
y = [4, 1, 3, 6]
plt.scatter(x, y, c='green')
 
x = [5, 6, 7, 8]
y = [1, 3, 5, 2]
plt.scatter(x, y, c='red')

plt.show()
