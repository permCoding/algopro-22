[
    [1, 2, 3], 
    [4, 5, 6, 5666, 777, 888], 
    [7, 9]
]

a, b, c = [1, 2, 3], [4, 5, 6, 66,77,88], [7, 9]

tab = [a, b, c]

for row in range(len(tab)):
    for col in range(len(tab[row])):
        print(tab[row][col], end=' ')
    print()
