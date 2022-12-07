from random import randint as r


count = 10
lst = []
for _ in range(count):
    lst.append(r(1, 100))

print(lst)

amount = 0
for elm in lst:
    if elm%2 != 0:
        amount += 1
print(amount)

amount = 0
for index in range(len(lst)):
    if lst[index]%2 != 0:
        amount += 1
print(amount)