lst = [i for i in range(10)]

print(lst)

lst[0] = lst[1]
print(lst)

lst[len(lst)-1] = 666
print(lst)

last = lst.pop()
print(lst, last)

